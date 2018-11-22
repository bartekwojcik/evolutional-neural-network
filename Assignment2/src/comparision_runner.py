from src.Gas.ga_runner import run_ga
from src.Pso.Pso_runner import run_pso
import matplotlib.pyplot as plt

def combined_plot(ga, pso, labels, title, comparision):
    plt.plot(ga.keys(), ga.values(), label="GA")
    plt.plot(pso.keys(), pso.values(), label="PSO")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
    name = title + " (" + labels + ") Comparision " + str(comparision)
    plt.title(name)
    plt.savefig("partial\\"+name+ ".jpg")
    plt.clf()

def run_comparision(comparision_number, iterations, functions, popsize):
    gas_bests = []
    gas_averages = []

    # run gas
    for tuple in functions:
        f = tuple[0]
        ga_bests, ga_average, ga_worst, ga_last_pop = run_ga(f, popsize, iterations)
        gas_bests.append(ga_bests)
        gas_averages.append(ga_average)

    pso_bests = []
    pso_averages = []
    # run pso
    for tuple in functions:
        f = tuple[0]
        averages, bests = run_pso(f, popsize, iterations)
        pso_bests.append(bests)
        pso_averages.append(averages)

    for i in range(len(functions)):
        pso_b = pso_bests[i]
        pso_a = pso_averages[i]
        ga_b = gas_bests[i]
        ga_a = gas_averages[i]
        function_name = functions[i][1]
        combined_plot(ga_b, pso_b, "best", function_name,comparision_number)
        combined_plot(ga_a, pso_a, "average", function_name, comparision_number)


    return gas_bests,gas_averages,pso_bests,pso_averages
