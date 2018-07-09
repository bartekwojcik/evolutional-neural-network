import numpy as np
from population_processor import Population_processor
import matplotlib.pyplot as plt
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
    ind_list = []

    file_helper.get_OR_data()
    pop_processor = Population_processor()




if __name__ == "__main__": main()
