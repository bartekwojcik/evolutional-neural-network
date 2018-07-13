import numpy as np
from population_processor import Population_processor
import matplotlib.pyplot as plt
from chromosoms_provider import Chromosomes_providers
import file_helper

def simple_plot(x, y, label):
    plt.scatter(x, y, s=1,
                label=label)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)


#todo preprocess data!!! use scalers, shuffle etc
def main():

    popsize = 100
    maxgen = int(100)
    chrom_provider = Chromosomes_providers()

    train_x, train_y = file_helper.get_OR_data()
    pop_processor = Population_processor(train_x,train_y,popsize,maxgen,chromosomes_provider=chrom_provider)
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
    plt.ioff()
    plt.show()
    aaaa = bests.values()
    print(*aaaa)


if __name__ == "__main__": main()
