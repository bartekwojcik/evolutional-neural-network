from optproblems.cec2005 import *
from src.Gas.ga_runner import run_ga


def main():

    functions = [F1(2),F3(2),F5(2),F8(2),F11(2)]

    for f in functions:
        ga_bests, ga_average, ga_worst, ga_last_pop = run_ga(f)
        debug = 5



