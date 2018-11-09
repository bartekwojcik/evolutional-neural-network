import numpy as np
import math
import random
class Particle():

    def __init__(self, function_provider, beta, gamma, sigma):
        '''
        :param weights: [beta,gamma,sigma]
        '''
        #it is always two as have to be consistent with earlier implementation of problems and genetic algorightms
        self.dimensions = 2
        self.function_provider = function_provider
        self.velocity = []
        self.informants = []
        self.position_best_informants = []
        self.position_best_individual = []
        self.individual_best_fitness = None
        self.position = [0,0]
        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma

        # function_boundries: tuple - (max_x,max_y),(min_x,min_y)
        bounds = self.function_provider.get_range()
        for i in range(self.dimensions):
            #setting particles initial velocity to zero
            #https://www.researchgate.net/post/What_is_the_best_way_to_initialize_the_velocity_in_PSO_algorithm_Is_there_any_relation_with_position_number_of_particle_dimension_of_the_problem
            self.velocity.append(0)
            self.position[i] = random.uniform(bounds[1][i],bounds[0][i])

    def fitness_value(self):
        return self.function_provider.calc_funct(self.position[0],self.position[1])


    def update_velocity(self, global_best_position, alpha):

        for i in range(self.dimensions):
            b = random.uniform(0, self.beta)
            c = random.uniform(0, self.gamma)
            d = random.uniform(0, self.sigma)

            part_b = b * (self.position_best_individual[i] - self.position[i])
            part_c = c * (self.position_best_informants[i] - self.position[i])
            part_d = d * (global_best_position[i] - self.position[i])
            self.velocity[i] = alpha*self.velocity[i] + part_b + part_c + part_d

    def update_position(self):
        # function_boundries: tuple - (max_x,max_y),(min_x,min_y)
        bounds = self.function_provider.get_range()
        for i in range(self.dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            max = bounds[0][i]
            min = bounds[1][i]

            if self.position[i] > max:
                self.position[i] = max
            elif self.position[i] < min:
                self.position[i] = min






