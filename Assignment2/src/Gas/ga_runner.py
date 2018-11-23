import numpy as np
from src.math_functions import *
from src.Gas import file_helper
from src.Gas.population_processor import Population_processor
import matplotlib.pyplot as plt
from src.Gas.chromosoms_provider import Chromosomes_providers
from optproblems.cec2005 import *

def simple_plot(x, y, label):
    plt.scatter(x, y, s=1,
                label=label)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)


def run_ga(function,popsize,maxgen):

    chrom_provider = Chromosomes_providers()
    chrom_provider.function_wrapper = FunctionProvider(function)
    pop_processor = Population_processor(popsize,
                                         maxgen,
                                         retain_percentage=0.3,
                                         mutate_chance= 0.05,
                                         alpha_blend= 0.5,
                                         chromosomes_provider=chrom_provider)
    generator = pop_processor.start_evolution()
    worsts = {}
    bests = {}
    best_inds = {}
    averages = {}

    for idx,population in generator:
        average = population.average()
        best_ind = population.best()
        best = best_ind.fitness_value()
        worst = population.worst().fitness_value()
        worsts[idx] = float(worst)
        bests[idx] = best
        averages[idx] = average
        best_inds[idx] = best_ind
        last_pop =  population
       # del population

    return bests,averages,worsts,last_pop
