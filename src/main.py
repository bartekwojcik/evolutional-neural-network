from optproblems.cec2005 import *
from src.Gas.ga_runner import run_ga
from src.Pso.Pso_runner import run_pso
import matplotlib.pyplot as plt

def simple_plot(x, y, label):
    plt.scatter(x, y, s=1,
                label=label)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

def combined_scatter(ga,pso,labels):
    plt.plot(ga.keys(),ga.values(),label="genetic: " + labels)
    plt.plot(pso.keys(), pso.values(), label="particles: " + labels)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)


def main():

    functions = [F1(2),F3(2),F5(2),F8(2),F11(2)]
    iterations = 400
    #should be even
    popsize = 100

    gas_bests=[]
    gas_averages=[]

    #run gas
    for f in functions:
        ga_bests, ga_average, ga_worst, ga_last_pop = run_ga(f, popsize,iterations)
        gas_bests.append(ga_bests)
        gas_averages.append(ga_average)

    pso_bests = []
    pso_averages = []
    #run pso
    for f in functions:
        averages, bests = run_pso(f,popsize,iterations)
        pso_bests.append(bests)
        pso_averages.append(averages)

    for i in range(len(functions)):
        pso_b = pso_bests[i]
        pso_a = pso_averages[i]
        ga_b = gas_bests[i]
        ga_a = gas_averages[i]
        combined_scatter(ga_b,pso_b,"bests (" + str(i) + ")")
        plt.show()
        combined_scatter(ga_a, pso_a, "average (" + str(i) + ")")
        plt.show()



main()




