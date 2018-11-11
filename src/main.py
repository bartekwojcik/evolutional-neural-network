from src.comparision_runner import run_comparision
from optproblems.cec2005 import *
import matplotlib.pyplot as plt
import numpy as np

def combined_plot(ga, pso, description):
    plt.plot(ga, label="GA")
    plt.plot(pso, label="PSO")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
    plt.title(description)
    plt.savefig(description+ ".jpg")
    plt.clf()

functions = [(F1(2), "F1"), (F3(2), "F3"), (F5(2), "F5"), (F8(2), "F8"), (F11(2), "F11")]
# should be even
popsize = 100
number_of_comparisons = 4
number_of_functions = len(functions)
number_of_iterations = 50


trials_gas_best = []
trials_gas_average = []
trials_pso_best = []
trials_pso_average = []


#this is the entry point for my function
#and this is also one of the ugliest and slopiest codes i have ever wrote

for i in range(number_of_comparisons):
    gas_bests, gas_averages, pso_bests, pso_averages = run_comparision(i,number_of_iterations, functions,popsize)
    trials_gas_average.append(gas_averages)
    trials_gas_best.append(gas_bests)
    trials_pso_average.append(pso_averages)
    trials_pso_best.append(pso_bests)

trials_gas_best = np.array(trials_gas_best)
trials_gas_average= np.array(trials_gas_average)
trials_pso_best= np.array(trials_pso_best)
trials_pso_average= np.array(trials_pso_average)

average_gas_bests = np.zeros((number_of_functions, number_of_iterations))
average_gas_average = np.zeros((number_of_functions, number_of_iterations))
average_pso_bests = np.zeros((number_of_functions, number_of_iterations))
average_pso_average = np.zeros((number_of_functions, number_of_iterations))

for c in range(number_of_comparisons):
    for f in range(number_of_functions):
        for i in range(number_of_iterations):
            average_gas_bests[f,i] += trials_gas_best[c,f][i]
            average_gas_average[f, i] += trials_gas_average[c, f][i]
            average_pso_bests[f, i] += trials_pso_best[c, f][i]
            average_pso_average[f, i] += trials_pso_average[c, f][i]

average_gas_bests  /= number_of_iterations
average_gas_average /= number_of_iterations
average_pso_bests /= number_of_iterations
average_pso_average /= number_of_iterations

debug = 5

for f in range(number_of_functions):
    description_bests = "Final average best values function" + functions[f][1]
    description_average = "Final average average values function" + functions[f][1]
    combined_plot(average_gas_bests[f], average_pso_bests[f],description_bests)
    combined_plot(average_gas_average[f], average_pso_average[f],description_average)