import numpy as np
import random

class Individual(object):

    def __init__(self, train_x, train_y, valid_x, valid_y, chromosomes=None, random_chrom_provider=None):
        if chromosomes is not None:
            self.weights = chromosomes.weights
            self.activation_function = chromosomes.act_func
            #todo add later
            #self.neurons_first_layer = chromosomes.neurons_first_layer
            #todo add later
            #self.number_hidden_layers = chromosomes.number_hidden_layers
            self.num_neur_hidden_layer = chromosomes.num_neur_hidden_layer
        else:
            self.random_chrom_provider = random_chrom_provider
            self.set_random_chromosomes()

        #todo train


    def fitness_value(self):
        # todo return accuracy
        return self.value_function()

    def relative_fitness(self, pop_fitness):
        result = self.fitness_value() / pop_fitness
        return result

    def set_random_chromosomes(self):
        values = self.random_chrom_provider
        #todo
        chromosome = 0
        return chromosome

    def mutate(self,mutation_rate):
        #todo
        prop = mutation_rate
        for c in range(0):
            rand = random.random()
            if rand <= prop:
                #todo
                pass





