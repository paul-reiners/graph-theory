import random
from unittest import TestCase

from vnc_matching_challenge.genetic_algorithm import crossover, mutation


class Test(TestCase):
    def test_crossover(self):
        parent1 = {'m1': 'f8',
                   'm2': 'f6',
                   'm3': 'f4',
                   'm4': 'f1',
                   'm5': 'f3',
                   'm6': 'f2',
                   'm7': 'f7',
                   'm8': 'f5'}
        parent2 = {'m1': 'f7',
                   'm2': 'f3',
                   'm3': 'f4',
                   'm4': 'f5',
                   'm5': 'f2',
                   'm6': 'f6',
                   'm7': 'f1',
                   'm8': 'f8'}
        child1, child2 = crossover(parent1, parent2)
        child1_diff_count = 0
        for key in child1.keys():
            if child1[key] != parent1[key]:
                child1_diff_count += 1
        self.assertEquals(2, child1_diff_count)
        child2_diff_count = 0
        for key in child2.keys():
            if child2[key] != parent2[key]:
                child2_diff_count += 1
        self.assertEquals(2, child2_diff_count)
        self.assertEquals(len(set(parent1.values())), len(set(child1.values())))
        self.assertEquals(len(set(parent2.values())), len(set(child2.values())))

    def test_mutation(self):
        random.seed(10)
        individual = {'m1': 'f8',
                      'm2': 'f6',
                      'm3': 'f4',
                      'm4': 'f1',
                      'm5': 'f3',
                      'm6': 'f2',
                      'm7': 'f7',
                      'm8': 'f5'}
        mutation_rate = 0.1
        mutated_individual = mutation(individual, mutation_rate)
        self.assertEquals(mutated_individual['m1'], 'f8')
        self.assertEquals(mutated_individual['m2'], 'f6')
        self.assertEquals(mutated_individual['m3'], 'f1')
        self.assertEquals(mutated_individual['m4'], 'f4')
        self.assertEquals(mutated_individual['m5'], 'f3')
        self.assertEquals(mutated_individual['m6'], 'f2')
        self.assertEquals(mutated_individual['m7'], 'f5')
        self.assertEquals(mutated_individual['m8'], 'f7')
        self.assertEquals(len(set(individual.values())), len(set(mutated_individual.values())))
