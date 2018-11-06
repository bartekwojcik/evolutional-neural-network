import numpy as np
import random
from src.Gas.mutators import normal_mutation

class Individual(object):

    def __init__(self, chromosomes=None, chrom_provider=None):
        """
        :param test_x: test values
        :param test_y: test targets
        :param chromosomes: dictionary of indivuals's parameters, can be null if you supply :random_chrom_provider
        :param random_chrom_provider: provides random chromosomes values
        """
        if chrom_provider is None and chromosomes is None:
            raise ValueError("chromosomes and provider are both null")

        self.chrom_provider = chrom_provider
        if chromosomes is not None:
            self.x = chromosomes.x
            self.y = chromosomes.y
            self.range_array = chromosomes.range_array
        else:
            self.set_random_chromosomes()

    def fitness_value(self):
        #i want negative value because later i am compering the highest value instea of the lowest
        return self.chrom_provider.function_wrapper.calc_funct(self.x,self.y)

    def relative_fitness(self, pop_fitness):
        if(pop_fitness == 0):
            return 0
        result = self.fitness_value() / pop_fitness
        return result

    def set_random_chromosomes(self):
        self.range_array = self.chrom_provider.function_wrapper.get_range()

        min_x = self.range_array[1][0]
        max_x = self.range_array[0][0]
        min_y = self.range_array[1][1]
        max_y = self.range_array[0][1]

        self.x = random.uniform(min_x,max_x)
        self.y = random.uniform(min_y,max_y)


    def mutate(self, mutate_chance):

        x = random.random()
        if x <= mutate_chance:
            self.x = normal_mutation(self.x)
        y = random.random()
        if y <= mutate_chance:
            self.y = normal_mutation(self.y)

    def keep_in_range(self):
        min_x = self.range_array[1][0]
        max_x = self.range_array[0][0]
        min_y = self.range_array[1][1]
        max_y = self.range_array[0][1]

        if self.x > max_x:
            self.x = max_x
        elif self.x < min_x:
            self.x = min_x

        if self.y > max_y:
            self.y = max_y
        elif self.y < min_y:
            self.y = min_y










