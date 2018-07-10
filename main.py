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

    popsize = 10
    maxgen = 10
    chrom_provider = Chromosomes_providers()

    train_x, train_y = file_helper.get_OR_data()
    pop_processor = Population_processor(train_x,train_y,popsize,maxgen,chromosomes_provider=chrom_provider)
    pop_processor.start_evolution()




if __name__ == "__main__": main()
