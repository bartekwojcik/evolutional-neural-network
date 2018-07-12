import numpy as np
import random
from neural_network import Network


class Individual(object):

    def __init__(self, test_x, test_y, chromosomes=None, random_chrom_provider=None):
        """
        :param test_x: test values
        :param test_y: test targets
        :param chromosomes: dictionary of network's parameters, can be null if you supply :random_chrom_provider
        :param random_chrom_provider: provides random chromosomes values
        """
        if chromosomes is not None:
            self.weights = chromosomes.weights
            self.activation_function = chromosomes.act_func
            # todo add later
            # self.neurons_first_layer = chromosomes.neurons_first_layer
            # todo add later
            # self.number_hidden_layers = chromosomes.number_hidden_layers
            self.num_neur_hidden_layer = chromosomes.num_neur_hidden_layer
        if random_chrom_provider is None and chromosomes is None:
            raise ValueError("chromosomes and provider are both null")
        else:
            self.random_chrom_provider = random_chrom_provider
            self.set_random_chromosomes(test_x, test_y)

        self.net = Network(test_x, test_y, self.weights, self.num_neur_hidden_layer, self.activation_function)
        self.accuracy = self.net.accuracy(test_x, test_y, 0.01, False)

    def fitness_value(self):
        return self.accuracy

    def relative_fitness(self, pop_fitness):
        if(pop_fitness == 0):
            return 0
        result = self.fitness_value() / pop_fitness
        return result

    def set_random_chromosomes(self, x, y):
        nin = np.shape(x)[1]
        nout = np.shape(y)[1]
        self.activation_function = self.random_chrom_provider.get_random_activation_function()
        self.num_neur_hidden_layer = random.randint(1,10)
        # todo this is not truly random, get with something better
        weights1 = (np.random.rand(nin + 1, self.num_neur_hidden_layer) - 0.5) * 2 / np.sqrt(nin)
        weights2 = (np.random.rand(self.num_neur_hidden_layer + 1, nout) - 0.5) * 2 / np.sqrt(
            self.num_neur_hidden_layer)

        self.weights = [weights1, weights2]

    def mutate(self, mutation_rate):
        # todo
        prop = mutation_rate
        for c in range(0):
            rand = random.random()
            if rand <= prop:
                # todo
                pass
