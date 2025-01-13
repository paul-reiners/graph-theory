import collections
import random
import numpy as np
import math

from calculate_alignment_score import FEMALE_GRAPH_FILE, MALE_GRAPH_FILE, MATCHING_FILE, calculate_alignment, load_edges, load_matching
from util import create_initial_population

male_edges = load_edges(MALE_GRAPH_FILE)
female_edges = load_edges(FEMALE_GRAPH_FILE)
matching = load_matching(MATCHING_FILE)

INFINITY = 1000000
POPULATION_SIZE = 200
 

def make_node():
    matching = load_matching(MATCHING_FILE)
    matching = collections.OrderedDict(sorted(matching.copy().items()))
    v_m_list = list(matching.keys())
    v_m_list.sort()
    v_f_list = list(matching.values())
    v_f_list.sort()

    initial_state = create_initial_population(POPULATION_SIZE, v_m_list, v_f_list)

    return initial_state

def randomly_selected_successor(current, T):
    current_copy = np.copy(current)
    prob = T / INFINITY
    for i in range(len(current_copy) - 1):
        for j in range(i + 1, len(current_copy)):
            key_list = list(current.keys())
            if random.randon() < prob:
                temp_key = key_list[i]
                temp_val = current_copy[temp_key]
                key_1 = current_copy[key_list[i]]
                key_2 = current_copy[key_list[2]]
                val_2 = current_copy[key_2]
                current_copy[key_1] = val_2
                current_copy[key_2] = temp_val

    return current_copy

            



def schedule(t):
    return t - 1


def simulated_annealing(problem, schedule):  # returns a solution state
    # inputs:
    #   problem, a problem
    #   schedule, a mapping from time to "temperature"

    current = make_node()
    for t in range(INFINITY):
        T = schedule(t)
        if T == 0:
            return current
        next = randomly_selected_successor(current, T)
        delta_e = next.value - current.value
        if delta_e > 0: 
            current = next
        else:
            prob = math.exp(delta_e, T)
            if random.random() < prob:
                current = next 
            