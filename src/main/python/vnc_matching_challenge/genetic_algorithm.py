import random
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable

from src.main.python.vnc_matching_challenge.calculate_alignment_score import calculate_alignment


# Define the fitness function (objective with the objective of aligning the
# connectivity between the two graph as closely as possible.
def fitness_function(male_edges, female_edges, matching):
    return calculate_alignment(male_edges, female_edges, matching)
