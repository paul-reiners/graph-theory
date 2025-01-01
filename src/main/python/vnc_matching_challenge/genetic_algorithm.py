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
