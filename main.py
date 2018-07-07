import numpy as np
from neural_network import Network
import random
import math
import matplotlib.pyplot as plt
from individual import Individual
from population import Population

#todo preprocess data!!! use scalers, shuffle etc
def main():

    popsize = 20
    maxgen = 500
    ind_list = []
    for i in range(popsize):
        ind = Individual(weird_function, allels_num, st)
        ind_list.append(ind)

    initial_values = list(map(lambda ind: ind.fitness_value(), ind_list))
    initial_decodings = list(map(lambda ind: ind.decode_individual(), ind_list))
    pop_list = []

    # main loop
    for j in range(maxgen):
        population = Population(st, ind_list)
        pop_fitness = population.whole_pop_fitness()
        test = sum(list(map(lambda ind: ind.relative_fitness(pop_fitness), ind_list)))
        assert math.fabs(test - 1) <= 1e-7, "probability must sum to one!"
        dens = population.get_pop_fitness_density()
        mating_pool = population.get_mating_pool(dens)
        random.shuffle(mating_pool)
        ind_list = population.breed_population(mating_pool, allels_num, weird_function)
        pop_list.append(population)

    last_decodings = list(map(lambda ind: ind.decode_individual(), ind_list))
    last_values = list(map(lambda ind: ind.fitness_value(), ind_list))

    print('final max value:')
    print(max(last_values))
    print('final max decoding:')
    print(max(last_decodings))

    best_of_current_population = {}
    best_so_far = 0
    average_of_current_population = {}
    worst_of_current_population = {}

    for idx, pop in enumerate(pop_list):
        fitness_list = [ind.fitness_value() for ind in pop.individuals]
        best = max(fitness_list)
        best_of_current_population[idx] = best
        average_of_current_population[idx] = sum(fitness_list) / float(len(fitness_list))
        worst_of_current_population[idx] = min(fitness_list)
        if best > best_so_far:
            best_so_far = best

    def simple_plot(x, y, label):
        plt.scatter(x, y, s=1,
                    label=label)
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)

    # plot best of current population
    plt.subplot(211)
    simple_plot(best_of_current_population.keys(), best_of_current_population.values(),
                label="best of current population")

    # plt.ylim(0,4)
    plt.xlim(0, len(best_of_current_population.keys()))
    # plot average of population
    plt.subplot(212)
    simple_plot(average_of_current_population.keys(), average_of_current_population.values(),
                label="average of population")

    plt.figure()
    # plot worst of population
    plt.subplot(211)
    simple_plot(worst_of_current_population.keys(), worst_of_current_population.values(),
                label="worst of current population")

    # initial / last values plot
    plt.subplot(212)
    line, = plt.plot(x, f, lw=2)
    plt.plot(last_decodings, last_values, 'ro', label="last values")
    plt.plot(initial_decodings, initial_values, 'bo', label="initial values")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
    plt.xlim(-1, 2)
    plt.ioff()
    plt.show()


if __name__ == "__main__": main()
