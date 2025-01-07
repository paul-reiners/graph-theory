import numpy as np
from scipy.optimize import dual_annealing

from modules.calculate_alignment_score import FEMALE_GRAPH_FILE, MALE_GRAPH_FILE, MATCHING_FILE, calculate_alignment, load_edges, load_matching

male_edges = load_edges(MALE_GRAPH_FILE)
female_edges = load_edges(FEMALE_GRAPH_FILE)
func = lambda matching: -calculate_alignment(male_edges, female_edges, matching)
matching = load_matching(MATCHING_FILE)
ret = dual_annealing(func, male_edges=male_edges, female_edges=female_edges, matching=matching)
ret.x
ret.fun
