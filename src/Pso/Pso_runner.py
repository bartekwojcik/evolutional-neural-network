from optproblems.cec2005 import *
from src.Pso.particle import Particle
from src.math_functions import *
import numpy as np

def run_pso(function,popsize,iterations):
    function_provider = FunctionProvider(function)
    #https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4436220/

    alpha = 0.5
    beta = 1
    gamma = 1.5
    sigma = 1.5
    global_best = None
    global_best_position = []
    particles= []
    number_of_informants = int(popsize/20)

    #create new particles
    for _ in range(popsize):
        new_particle = Particle(function_provider,beta,gamma,sigma)
        particles.append(new_particle)

    #select informants to each particle
    for p in particles:
        informant_indices = np.random.randint(0,popsize,size=number_of_informants)
        for inf_idx in informant_indices:
            informant = particles[inf_idx]
            if informant != p:
                p.informants.append(informant)

    bests_per_iter = {}
    average_per_iter = {}
    #iterate
    for iter in range(iterations):
        #evaluete fitness
        this_iter_values = []
        for p in particles:
            value = p.fitness_value()
            this_iter_values.append(value)
            #update best individual value
            if p.individual_best_fitness is None or value > p.individual_best_fitness:
                p.individual_best_fitness = value
                p.position_best_individual = p.position

            #update global value
            if global_best is None or value > global_best :
                global_best = value
                global_best_position = p.position

            #update best informant
            p_informants = p.informants

            best_informant_dict =[(inf.fitness_value(), inf) for inf in p_informants]
            best_dict_ordered = [key_value_pair for key_value_pair in
                                sorted(best_informant_dict , key=lambda x: x[0], reverse=True)]
            p.position_best_informants = best_dict_ordered[0][1].position

        average_per_iter[iter] =  np.mean(this_iter_values)
        bests_per_iter[iter] = np.max(this_iter_values)


        #evaluate position
        for p in particles:
            p.update_velocity(global_best_position, alpha)
            p.update_position()


    print(global_best)
    print("coordinates: ", *global_best_position)
    return average_per_iter, bests_per_iter



