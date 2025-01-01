import copy
import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

from src.main.python.vnc_matching_challenge.calculate_alignment_score import calculate_alignment


# Define the fitness function with the objective of aligning the
# connectivity between the two graph as closely as possible.
def fitness_function(male_edges, female_edges, matching):
    return calculate_alignment(male_edges, female_edges, matching)


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


# Mutation function
def mutation(individual, mutation_rate):
    individual_copy = copy.deepcopy(individual)
    for i in range(len(individual_copy.keys())):
        for j in range(i + 1, len(individual_copy.keys())):
            if random.random() < mutation_rate:
                key_1 = list(individual_copy.keys())[i]
                value1 = individual_copy[key_1]
                key_2 = list(individual_copy.keys())[j]
                value2 = individual_copy[key_2]
                individual_copy[key_1] = value2
                individual_copy[key_2] = value1

    return individual_copy
