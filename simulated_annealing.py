import collections
import random
import numpy as np
import math

from calculate_alignment_score import FEMALE_GRAPH_FILE, MALE_GRAPH_FILE, MATCHING_FILE, calculate_alignment, load_edges, load_matching
from util import create_individual, create_initial_population

INFINITY = 100


def make_node() -> dict:
    """
    Create the initial state for the simulated annealing process.
    Returns a dictionary representing the initial matching.
    """
    try:
        matching = load_matching(MATCHING_FILE)
        matching = collections.OrderedDict(sorted(matching.items()))
        male_nodes = sorted(matching.keys())
        female_nodes = sorted(matching.values())
        return create_individual(male_nodes, female_nodes)
    except Exception as e:
        raise RuntimeError(f"Error creating initial state: {e}")


def randomly_selected_successor(current: dict, swap_prob: float = 0.05) -> dict:
    """
    Generate a successor state by swapping pairs of matches with a given probability.
    """
    new_state = current.copy()
    keys = list(current.keys())

    for i in range(len(keys) - 1):
        if random.random() < swap_prob:
            j = random.randint(i + 1, len(keys) - 1)
            key_1, key_2 = keys[i], keys[j]
            new_state[key_1], new_state[key_2] = new_state[key_2], new_state[key_1]

    return new_state


def schedule(t: int) -> float:
    """
    Define a cooling schedule for simulated annealing.
    """
    return max(1e-10, 100 - t)  # Avoid zero or negative temperatures


def simulated_annealing(schedule) -> tuple:
    """
    Perform simulated annealing to find the best alignment.
    Returns the best state and its alignment score.
    """
    male_edges = load_edges(MALE_GRAPH_FILE)
    female_edges = load_edges(FEMALE_GRAPH_FILE)

    try:
        current = make_node()
    except RuntimeError as e:
        print(e)
        return None, None

    for t in range(INFINITY):
        T = schedule(t)
        if T <= 1e-10:  # Stop if temperature is effectively zero
            return current, calculate_alignment(male_edges, female_edges, current)

        next_state = randomly_selected_successor(current)
        current_alignment = calculate_alignment(male_edges, female_edges, current)
        next_alignment = calculate_alignment(male_edges, female_edges, next_state)

        delta_e = next_alignment - current_alignment
        if delta_e > 0 or random.random() < math.exp(delta_e / T):
            current = next_state

    return current, calculate_alignment(male_edges, female_edges, current)


if __name__ == "__main__":
    schedule_fn = lambda t: max(1e-10, 100 - t)  # Ensure a non-zero temperature
    best_matching, best_alignment = simulated_annealing(schedule_fn)

    if best_matching is not None:
        print(f"Best Matching: {best_matching}")
        print(f"Best Alignment Score: {best_alignment}")
    else:
        print("Failed to find a solution.")
