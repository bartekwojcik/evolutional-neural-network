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
        if random_chrom_provider is None and chromosomes is None:
            raise ValueError("chromosomes and provider are both null")

        self.random_chrom_provider = random_chrom_provider
        if chromosomes is not None:
            self.weights = chromosomes.weights
            self.activation_function = chromosomes.act_func
            # todo add later
            # self.neurons_first_layer = chromosomes.neurons_first_layer
            # todo add later
            # self.number_hidden_layers = chromosomes.number_hidden_layers
            self.num_neur_hidden_layer = chromosomes.num_neur_hidden_layer

        else:
            self.set_random_chromosomes(test_x, test_y)

        self.x = test_x
        self.y = test_y

        self.net = Network(test_x, test_y, self.weights, self.num_neur_hidden_layer, self.activation_function)
        self.accuracy = self.net.accuracy(test_x, test_y, 0.05, False)

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
        #todo this is part of topology as well, change it when you will be changing layers as well
        # self.num_neur_hidden_layer = random.randint(1,10)
        self.num_neur_hidden_layer = 5
        # todo this is not truly random, get with something better
        weights1 = (np.random.rand(nin + 1, self.num_neur_hidden_layer) - 0.5) * 2 / np.sqrt(nin)
        weights2 = (np.random.rand(self.num_neur_hidden_layer + 1, nout) - 0.5) * 2 / np.sqrt(
            self.num_neur_hidden_layer)

        self.weights = [weights1, weights2]

    def mutate(self, mutate_chance,nonuni_mut_temp):
        # mutate activation function
        x = random.random()
        if x <= mutate_chance:
            self.activation_function = self.random_chrom_provider.get_random_activation_function()

        self.mutate_weights(mutate_chance, nonuni_mut_temp)

    def mutate_weights(self, mutate_chance, nonuni_mut_temp):
        # mutate weights using Nonuniform Mutation and Normal Mutation mix
        new_weights = []
        for weight in self.weights:
            shape = weight.shape
            # mean and standard deviation
            #Normal Mutation
            mu, sigma = 0, 0.1
            N01 = np.random.normal(mu, sigma, shape)
            n_w = weight + sigma * N01
            new_weights.append(n_w)
        test_net = Network(self.x, self.y, new_weights, self.num_neur_hidden_layer, self.activation_function)
        #Nonuniform Mutation
        test_acc = test_net.accuracy(self.x, self.y, 0.05, False)
        if test_acc >= self.accuracy:
            self.weights = new_weights
        else:
            prob = (test_acc - self.accuracy) / nonuni_mut_temp
            if prob <= mutate_chance:
                self.weights = new_weights



