import copy
import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
from functools import partial
import pandas as pd
import time
import tqdm
import collections

from vnc_matching_challenge.calculate_alignment_score import calculate_alignment, MATCHING_FILE, \
    load_matching, MALE_GRAPH_FILE, load_edges, FEMALE_GRAPH_FILE, DATA_DIR


# Define the fitness function with the objective of aligning the
# connectivity between the two graph as closely as possible.
def fitness_function(matching):
    return calculate_alignment(MALE_EDGES, FEMALE_EDGES, matching)


# Create the initial population
def create_initial_population(size, v_m_list, v_f_list):
    population = []
    population.append(matching)
    for _ in range(size - 1):
        v_f_list_copy = copy.deepcopy(v_f_list)
        random.shuffle(v_f_list_copy)
        individual = {v_m_list[i]: v_f_list_copy[i] for i in range(len(v_m_list))}
        individual = collections.OrderedDict(sorted(individual.copy().items()))
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
    f_values = list(parent1.values())
    random_values = random.sample(f_values, int(round(len(f_values) / 2)))
    child1 = parent1.copy()
    child2 = parent2.copy()

    for random_value in random_values:
        key_1 = get_key_by_value(parent1, random_value)
        key_2 = get_key_by_value(parent2, random_value)
        child1[key_2] = random_value
        child2[key_1] = random_value

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

    best_performers = []
    all_populations = []

    # Prepare for table
    table = PrettyTable()
    table.field_names = ["Generation", "Fitness"]

    for generation in tqdm.tqdm(range(generations), desc=" outer", position=0):
        fitnesses = [fitness_function(ind) for ind in population]

        # Store the best performer of the current generation
        best_individual = max(population, key=fitness_function)
        best_fitness = fitness_function(best_individual)
        best_performers.append((best_individual, best_fitness))
        all_populations.append(population[:])
        table.add_row([generation + 1, best_fitness])

        population = selection(population, fitnesses)

        next_population = []
        for i in tqdm.tqdm(range(0, len(population), 2), desc=" inner loop", position=1, leave=False):
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
    print(f'final_fitnesses: {final_fitnesses}')

    # Plot the values of a, b, and c over generations
    generations_list = range(1, len(best_performers) + 1)
    print(f'generations_list: {generations_list}')

    # Plot the fitness values over generations
    best_fitness_values = [fit[1] for fit in best_performers]
    print(f'best_fitness_values: {best_fitness_values}')
    min_fitness_values = [min([fitness_function(ind) for ind in population]) for population in all_populations]
    print(f'min_fitness_values: {min_fitness_values}')
    max_fitness_values = [max([fitness_function(ind) for ind in population]) for population in all_populations]
    print(f'max_fitness_values: {max_fitness_values}')

    return max(population, key=fitness_function)

def print_best_solution_file(best_solution, best_score):
    with open(f"{DATA_DIR}/vnc_matching_submission_reiners_{str(best_score).zfill(7)}.csv", "w") as file:
        file.write('Male Node ID,Female Node ID' + '\n')
        for key, value in best_solution.items():
            file.write(f'{key},{value}\n')

if __name__ == '__main__':
    start_time = time.time()

    MALE_EDGES = load_edges(MALE_GRAPH_FILE)
    FEMALE_EDGES = load_edges(FEMALE_GRAPH_FILE)

    # Parameters for the genetic algorithm
    population_size = 4
    generations = 2
    mutation_rate = 0.01

    # Run the genetic algorithm
    matching = load_matching(MATCHING_FILE)
    matching = collections.OrderedDict(sorted(matching.copy().items()))
    v_m_list = list(matching.keys())
    v_m_list.sort()
    v_f_list = list(matching.values())
    v_f_list.sort()
    best_solution = (
        genetic_algorithm(
            population_size, generations, mutation_rate, v_m_list, v_f_list))
    best_score = calculate_alignment(MALE_EDGES, FEMALE_EDGES, best_solution)
    print(f"Best score found: best_score = {best_score}")

    print_best_solution_file(best_solution, best_score)

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)
