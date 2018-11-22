from src.Gas.individual import Individual
from src.Gas.population import Population
from src.utils import My_Dict
import random


class Population_processor(object):
    def __init__(self, popsize,max_gen, chromosomes_provider,
                 retain_percentage=0.4, mutate_chance=0.1,
                 alpha_blend=0.5):
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


        self.alpha_blend = alpha_blend
        self.max_gen = max_gen
        self.popsize = popsize
        self.mutate_chance = mutate_chance
        self.retain_percentage = retain_percentage
        self.chromosomes_provider = chromosomes_provider

    def create_initial_population(self, popsize, mutations_params):
        """Create a population of random individuals.

        Args:
            popsize (int): population size

        Returns:
            Population: Population of individuals objects
        """
        pop = []
        for _ in range(0, popsize):
            ind = Individual(chrom_provider= self.chromosomes_provider)
            pop.append(ind)

        return Population(pop, popsize,mutations_params)

    def start_evolution(self):

        mutations_params = My_Dict()
        mutations_params.alpha_blend = self.alpha_blend
        mutations_params.mutate_chance = self.mutate_chance

        generation = self.create_initial_population(self.popsize,mutations_params)
        for i in range(self.max_gen):
            new_generation = generation.breed_new_population(self.retain_percentage)
            generation = new_generation
            yield i, new_generation

