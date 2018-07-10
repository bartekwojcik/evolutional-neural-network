from individual import Individual
from population import Population
import random


class Population_processor(object):
    def __init__(self, test_x, test_y, popsize,max_gen, chromosomes_provider, retain_percentage=0.1, mutate_chance=0.02):
        """Create an optimizer.

        Args:
            test_x (nparray): test values
            test_y (nparray): test targets
            popsize (int): population size
            max_gen (int): maximum number of generations
            chromosomes_provider (Chromosoms_providers): Possible network paremters
            retain (float): Percentage of population to retain after each generation
            mutate_chance (float): Probability a network chromosome will be randomly mutated

        """
        self.max_gen = max_gen
        self.popsize = popsize
        self.test_x = test_x
        self.test_y = test_y
        self.mutate_chance = mutate_chance
        self.retain_percentage = retain_percentage
        self.chromosomes_provider = chromosomes_provider

    def create_initial_population(self, popsize):
        """Create a population of random networks.

        Args:
            popsize (int): population size

        Returns:
            Population: Population of network objects
        """
        pop = []
        for _ in range(0, popsize):
            # Create a random network.
            # todo init paramters
            ind = Individual(self.test_x, self.test_y,random_chrom_provider= self.chromosomes_provider)
            # Add the network to our population.
            pop.append(ind)

        return Population(pop, popsize)

    def start_evolution(self):
        """
        Temporarly return list of all populations
        :return:
        """
        generation = self.create_initial_population(self.popsize)
        pop_list= []
        for i in range(self.max_gen):
            new_generation = generation.breed_new_population(self.retain_percentage)
            pop_list.append(new_generation)
        return pop_list

