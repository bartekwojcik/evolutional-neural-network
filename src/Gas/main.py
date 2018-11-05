import numpy as np
from src.math_functions import *
from src.Gas import file_helper
from src.Gas.population_processor import Population_processor
import matplotlib.pyplot as plt
from src.Gas.chromosoms_provider import Chromosomes_providers

def simple_plot(x, y, label):
    plt.scatter(x, y, s=1,
                label=label)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)


#todo preprocess data!!! use scalers, shuffle etc
def main():

    #popsize must be even
    popsize = 100
    maxgen = int(1000)
    chrom_provider = Chromosomes_providers()
    chrom_provider.function_wrapper = MatyasFunctionProvider()
    pop_processor = Population_processor(popsize,maxgen,chromosomes_provider=chrom_provider)
    generator = pop_processor.start_evolution()
    worsts = {}
    bests = {}
    averages = {}

    for idx,population in generator:
        average = population.average()
        best = population.best().fitness_value()
        worst = population.worst().fitness_value()
        worsts[idx] = float(worst)
        bests[idx] = best
        averages[idx] = average
        del population

    # plot best of current population
    plt.subplot(211)
    simple_plot(bests.keys(), bests.values(),
                label="best of current population")

    # plot average of population
    plt.subplot(212)
    simple_plot(averages.keys(), averages.values(),
                label="average of population")

    plt.figure()
    # plot worst of population
    plt.subplot(211)
    simple_plot(worsts.keys(), worsts.values(),
                label="worst of current population")
    #plt.ioff()
    plt.show()
    aaaa = bests.values()
    print(*aaaa)


if __name__ == "__main__": main()
