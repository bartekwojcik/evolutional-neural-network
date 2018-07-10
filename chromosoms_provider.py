from activations import *
import random

class Chromosomes_providers(object):
    def get_random_activation_function(self):
        """
        returns random activation function

        :return: random activation function
        """
        activations = [Sigmoid_activation(),Null_activation(),Cos_activation(),Tanh_activation(),Exp_activation()]
        random_activation = random.choice(activations)
        return random_activation
