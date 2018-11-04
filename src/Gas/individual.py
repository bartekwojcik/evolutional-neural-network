import numpy as np
import random

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
            pass


        else:
            self.set_random_chromosomes()


    def fitness_value(self):
        self.chrom_provider.function_wrapper.calc_funct(self.x,self.y)

    def relative_fitness(self, pop_fitness):
        if(pop_fitness == 0):
            return 0
        result = self.fitness_value() / pop_fitness
        return result

    def set_random_chromosomes(self):
        range_array = self.chrom_provider.function_wrapper.get_range()
        min_y = range_array[0][0]
        max_x= range_array[0][1]
        min_y = range_array[1][0]
        max_y= range_array[1][1]
        #todo assign self.x and self.y as random number from range


    def mutate(self, mutate_chance):
        x = random.random()
        if x <= mutate_chance:
            pass
            #todo mutate







