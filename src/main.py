from src.comparision_runner import run_comparision
import numpy as np


number_of_comparisons = 4
number_of_functions = 5



trials_gas_best = []
trials_gas_average = []
trials_pso_best = []
trials_pso_average = []

for i in range(number_of_comparisons):
    gas_bests, gas_averages, pso_bests, pso_averages = run_comparision(i)
    trials_gas_average.append(gas_averages)
    trials_gas_best.append(gas_bests)
    trials_pso_average.append(pso_averages)
    trials_pso_best.append(pso_bests)

trials_gas_best = np.array(trials_gas_best)
trials_gas_average= np.array(trials_gas_average)
trials_pso_best= np.array(trials_pso_best)
trials_pso_average= np.array(trials_pso_average)

debug = 5