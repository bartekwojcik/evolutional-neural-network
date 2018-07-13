from collections import OrderedDict
from individual import Individual
from mutators import *
import random


class Population(object):

    def __init__(self, individuals, popsize, mutations_params):
        self.mutations_params = mutations_params
        self.individuals = individuals
        self.popsize = popsize

    def whole_pop_fitness(self):
        pop_fitnesses = list(map(lambda ind: ind.fitness_value(), self.individuals))
        sum_pop_fitness = sum(pop_fitnesses)
        return sum_pop_fitness

    def get_pop_fitness_density(self):
        """Returns population's cumulative distribution function

        Returns: (list[float, Individual]): list of key-pair values where key is distribution and value is Individual
        """
        pop_fitness = self.whole_pop_fitness()
        d = list((i.relative_fitness(pop_fitness), i) for i in self.individuals)
        fit_list = sorted(d,key=lambda x: x[0])

        density = self.add_rec(fit_list[1:], [(fit_list[0])])
        return density

    def breed_mating_pool(self, mating_pool):
        """
        Crossovers parents in mating pool

        :param mating_pool: (list[Individuals]): list of Individuals

        :return: (list[Individuals]): list of offsprings
        """
        random.shuffle(mating_pool)
        offspring_list = []
        for i in range(0, len(mating_pool), 2):
            one = mating_pool[i]
            two = mating_pool[i + 1]
            off_one, off_two = self.crossover(one, two,self.mutations_params)

            offspring_list.append(off_one)
            offspring_list.append(off_two)
        return offspring_list

    def breed_new_population(self, retain_percentage):
        """len(best_ordered)
        Breed a new population (do next generation)
        :param:
        retain_percentage: (float) percent of best parents going to next population

        :return:
        (Population): new population object
        """
        fitness_dict = [(individual.fitness_value(), individual) for individual in self.individuals]
        best_ordered = [key_value_pair[1] for key_value_pair in sorted(fitness_dict, key=lambda x: x[0], reverse=True)]
        # Get the number we want to keep for the next gen.
        retain_length = int(len(best_ordered) * retain_percentage)
        parents = best_ordered[:retain_length]

        # Now find out how many spots we have left to fill.
        parents_length = len(parents)
        desired_length = self.popsize - parents_length
        density = self.get_pop_fitness_density()
        mating_pool = self.get_mating_pool(density,desired_length)
        #right now parents and mating pool may overlap, if you implement diffrent mating pool function (the better one) you dont need retain and parents
        mating_pool += parents

        children = self.breed_mating_pool(mating_pool)

        return Population(children,self.popsize, self.mutations_params)

    def crossover(self, mother, father, mutations_params):
        """Make two children as parts of their parents.

        Args:
            mother (dict): Network (Individuals) parameters
            father (dict): Network (Individuals) parameters

        Returns:
            (tuple): Two Individuals objects

        """
        #todo for tests, just return mother and father
        y1_d = {}
        y2_d = {}
        nnhl1 = mother.net.num_neur_hidden_layer
        nnhl2 = father.net.num_neur_hidden_layer

        #blend crossover over parents number of hidden layer neurons
        o1,o2 = blend_crossover(nnhl1,nnhl2,mutations_params.alpha_blend)
        y1_d.num_neur_hidden_layer = o1
        y2_d.num_neur_hidden_layer = o2

        # select activation functions from parents to offspring
        af1,af2 = select_activation_functions(mother.net.activation_function, father.activation.function)
        y1_d.act_func = af1
        y2_d.act_function = af2

        n = mutations_params.SBX_n

        #crossing over weights (todo still assuming weights len is the same)
        num_of_weights = mother.net.weights
        y1_d.weights = []
        y2_d.weights = []

        for w in range (num_of_weights):
            p1_weight = mother.net.weights[w]
            p2_weight = father.net.weights[w]
            o1,o2 = simulated_binary_crossover(p1_weight,p2_weight,n)
            y1_d.weights.append(o1)
            y2_d.weights.append(o2)


        y1 = Individual(mutations_params.test_x,
                        mutations_params.test_y,
                        y1_d)
        y2 = Individual(mutations_params.test_x,
                        mutations_params.test_y,
                        y2_d)

        return y1, y2


    def get_mating_pool(self, dens, lenght):
        """Return mating pool of given density using Roulette wheel selection

        :param dens: (list[float, Individual]): list of key-pair values where key is distribution and value is Individual
        lenght: amounts of parents selected

        :return: (list[Individual]): list of Individuals
        """
        #todo implement this thing that has arrows of roulette as many as populations
        mating_pool = []
        for i in range(lenght):
            rand = random.random()
            selected = next((x for x in dens if x[0] > rand),dens[-1])[1]
            mating_pool.append(selected)

        return mating_pool

    def average(self):
        """ Finds average fitness for this population

        :return:(float): average fitness of population
        """
        fitness_list = [ind.fitness_value() for ind in self.individuals]
        average_of_current_population = sum(fitness_list) / float(len(fitness_list))
        return average_of_current_population

    def best(self):
        """Finds best of population

        :return: (Individual): Individual with best fitness
        """
        best = max(self.individuals, key=lambda ind:ind.fitness_value())
        return best
    def worst(self):
        """Finds worst of population

        :return: (Individual): Individual with best fitness
        """
        worst = min(self.individuals, key=lambda ind:ind.fitness_value())
        return worst

    def add_rec(self,list, tail_list):
        if list:
            second_pair = list[0]
            last_existing = tail_list[-1]
            new_pair = (last_existing[0] + second_pair[0], second_pair[1])
            tail_list.append(new_pair)
            if list[1:]:
                self.add_rec(list[1:], tail_list)
        return tail_list