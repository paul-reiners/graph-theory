# Create the initial population
import collections
import copy
import random


def create_initial_population(size, v_m_list, v_f_list):
    population = []
    for _ in range(size):
        individual = create_individual(v_m_list, v_f_list)
        population.append(individual)
    return population

def create_individual(v_m_list, v_f_list):
    v_f_list_copy = copy.deepcopy(v_f_list)
    random.shuffle(v_f_list_copy)
    individual = {v_m_list[i]: v_f_list_copy[i] for i in range(len(v_m_list))}
    individual = collections.OrderedDict(sorted(individual.copy().items()))
    return individual
