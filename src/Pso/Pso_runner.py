from optproblems.cec2005 import *
from src.Pso.particle import Particle
from src.math_functions import *
import numpy as np

def run_pso(function):
    popsize = 200
    iterations = 500
    function_provider = FunctionProvider(function)
    #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4436220/

    alpha = 0.5
    beta = 2.5
    gamma = 2
    sigma = 1
    global_best = None
    position_global_best = []
    particles= []
    number_of_informants = int(popsize/20)

    #create new particles
    for _ in range(popsize):
        new_particle = Particle(function_provider,beta,gamma,sigma)
        particles.append(new_particle)

    #add informants to each particle
    for p in particles:
        informant_index = np.random.randint(0,popsize,size=number_of_informants)

    #iterate
    for iter in range(iterations):
        #evaluete fitness
        for p in particles:
            value = p.fitness_value()

            if value > p.individual_best_fitness or p.individual_best_fitness is None:
                p.individual_best_fitness = value
                p.individual_best_position = p.position
            if value > global_best or global_best is None:
                global_best = value
                position_global_best = p.position
        #evaluate position
        for p in particles:
            p.update_velocity(position_global_best, alpha)
            p.update_position()

