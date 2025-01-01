import copy
import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from functools import partial
import pandas as pd
import time

from src.main.python.vnc_matching_challenge.calculate_alignment_score import calculate_alignment, MATCHING_FILE, \
    load_matching, MALE_GRAPH_FILE, load_edges, FEMALE_GRAPH_FILE, DATA_DIR

start_time = time.time()

MALE_EDGES = load_edges(MALE_GRAPH_FILE)
FEMALE_EDGES = load_edges(FEMALE_GRAPH_FILE)


# Define the fitness function with the objective of aligning the
# connectivity between the two graph as closely as possible.
def fitness_function(matching):
    return calculate_alignment(MALE_EDGES, FEMALE_EDGES, matching)


# Create the initial population
def create_initial_population(size, v_m_list, v_f_list):
    population = []
    for _ in range(size):
        v_f_list_copy = copy.deepcopy(v_f_list)
        random.shuffle(v_f_list_copy)
        individual = {v_m_list[i]: v_f_list_copy[i] for i in range(len(v_m_list))}
        population.append(individual)
    return population


# Selection function using tournament selection
def selection(population, fitnesses, tournament_size=3):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected


def get_key_by_value(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            return key
    return None


# Crossover function
def crossover(parent1, parent2):
    # Single - point crossover
    f_values = list(parent1.values())
    random_values = random.sample(f_values, 2)
    value_1 = random_values[0]
    key_1_1 = get_key_by_value(parent1, value_1)
    value_2 = random_values[1]
    key_1_2 = get_key_by_value(parent1, value_2)
    key_2_1 = get_key_by_value(parent2, value_1)
    key_2_2 = get_key_by_value(parent2, value_2)

    child1 = parent1.copy()
    child1[key_1_1] = value_2
    child1[key_1_2] = value_1
    child2 = parent2.copy()
    child2[key_2_1] = value_2
    child2[key_2_2] = value_1

    return child1, child2


def mutation(individual, mutation_rate):
    # Create a deep copy to avoid modifying the original
    individual_copy = copy.deepcopy(individual)
    keys = list(individual_copy.keys())
    num_keys = len(keys)

    # Iterate through all pairs of keys
    for i in range(num_keys):
        for j in range(i + 1, num_keys):
            if random.random() < mutation_rate:
                # Swap the values of the two keys
                key_1, key_2 = keys[i], keys[j]
                individual_copy[key_1], individual_copy[key_2] = individual_copy[key_2], individual_copy[key_1]

    return individual_copy


# Main genetic algorithm function
def genetic_algorithm(population_size, generations, mutation_rate, v_m_list, v_f_list):
    population = create_initial_population(population_size, v_m_list, v_f_list)

    # Prepare for plotting
    fig, axs = plt.subplots(3, 1, figsize=(12, 18))  # 3 rows, 1 column for subplots
    best_performers = []
    all_populations = []

    # Prepare for table
    table = PrettyTable()
    table.field_names = ["Generation", "Fitness"]

    for generation in range(generations):
        fitnesses = [fitness_function(ind) for ind in population]

        # Store the best performer of the current generation
        best_individual = max(population, key=fitness_function)
        best_fitness = fitness_function(best_individual)
        best_performers.append((best_individual, best_fitness))
        all_populations.append(population[:])
        table.add_row([generation + 1, best_fitness])

        population = selection(population, fitnesses)

        next_population = []
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            child1, child2 = crossover(parent1, parent2)

            next_population.append(mutation(child1, mutation_rate))
            next_population.append(mutation(child2, mutation_rate))

        # Replace the old population with the new one, preserving the best individual
        next_population[0] = best_individual
        population = next_population

    # Print the table
    print(table)

    # Plot the population of one generation (last generation)
    final_population = all_populations[-1]
    final_fitnesses = [fitness_function(ind) for ind in final_population]

    axs[0].scatter(range(len(final_population)), [ind[0] for ind in final_population], color='blue', label='a')
    axs[0].scatter([final_population.index(best_individual)], [best_individual[0]], color='cyan', s=100,
                   label='Best Individual a')
    axs[0].set_ylabel('a', color='blue')
    axs[0].legend(loc='upper left')

    axs[1].scatter(range(len(final_population)), [ind[1] for ind in final_population], color='green', label='b')
    axs[1].scatter([final_population.index(best_individual)], [best_individual[1]], color='magenta', s=100,
                   label='Best Individual b')
    axs[1].set_ylabel('b', color='green')
    axs[1].legend(loc='upper left')

    axs[2].scatter(range(len(final_population)), [ind[2] for ind in final_population], color='red', label='c')
    axs[2].scatter([final_population.index(best_individual)], [best_individual[2]], color='yellow', s=100,
                   label='Best Individual c')
    axs[2].set_ylabel('c', color='red')
    axs[2].set_xlabel('Individual Index')
    axs[2].legend(loc='upper left')

    axs[0].set_title(f'Final Generation ({generations}) Population Solutions')

    # Plot the values of a, b, and c over generations
    generations_list = range(1, len(best_performers) + 1)

    # Plot the fitness values over generations
    best_fitness_values = [fit[1] for fit in best_performers]
    min_fitness_values = [min([fitness_function(ind) for ind in population]) for population in all_populations]
    max_fitness_values = [max([fitness_function(ind) for ind in population]) for population in all_populations]
    fig, ax = plt.subplots()
    ax.plot(generations_list, best_fitness_values, label='Best Fitness', color='black')
    ax.fill_between(generations_list, min_fitness_values, max_fitness_values, color='gray', alpha=0.5,
                    label='Fitness Range')
    ax.set_xlabel('Generation')
    ax.set_ylabel('Fitness')
    ax.set_title('Fitness Over Generations')
    ax.legend()

    # Create a subplot for the colorbar
    cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])  # [left, bottom, width, height]
    norm = plt.cm.colors.Normalize(vmin=0, vmax=generations)
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])
    fig.colorbar(sm, ax=ax, cax=cax, orientation='vertical', label='Generation')

    plt.show()

    return max(population, key=fitness_function)


# Parameters for the genetic algorithm
population_size = 100
generations = 20
mutation_rate = 0.01

# Run the genetic algorithm
matching = load_matching(MATCHING_FILE)
v_m_list = list(matching.keys())
v_m_list.sort()
v_f_list = list(matching.values())
v_f_list.sort()
best_solution = (
    genetic_algorithm(
        population_size, generations, mutation_rate, v_m_list, v_f_list))
print(f"Best solution found: best_solution = {best_solution}")
best_score = calculate_alignment(MALE_EDGES, FEMALE_EDGES, best_solution)
df = pd.DataFrame.from_dict(best_solution)
df.to_csv(f"{DATA_DIR}/vnc_matching_submission_reiners_{str(best_score).zfill(7)}.csv", index=False)

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)
