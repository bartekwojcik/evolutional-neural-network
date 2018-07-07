from collections import OrderedDict
from individual import Individual
import random


class Population(object):

    def __init__(self, individuals):
        self.individuals = individuals

    def whole_pop_fitness(self):
        pop_fitnesses = list(map(lambda ind: ind.fitness_value(), self.individuals))
        sum_pop_fitness = sum(pop_fitnesses)
        return sum_pop_fitness

    def get_pop_fitness_density(self):
        # discovering python's collections, lol

        pop_fitness = self.whole_pop_fitness()
        d = list((i.relative_fitness(pop_fitness), i) for i in self.individuals)
        fit_list = d

        density = self.add_rec(fit_list[1:], [(fit_list[0])])
        return density

    def breed_population(self, mating_pool, allels_num, eval_func):
        offspring_list = []
        for i in range(0, len(mating_pool), 2):
            one = mating_pool[i]
            two = mating_pool[i + 1]
            off_one, off_two = self.breed(one, two, allels_num, eval_func)

            offspring_list.append(off_one)
            offspring_list.append(off_two)
        return offspring_list

    def breed(self,  mother, father):
        """Make two children as parts of their parents.

        Args:
            mother (dict): Network parameters
            father (dict): Network parameters

        Returns:
            (list): Two network objects

        """
        point = 6#random.randint(1, allels_num - 1)
        all_one = one.chromosome
        all_two = two.chromosome

        half_one = all_one[:point]
        one_half = all_one[point:]

        half_two = all_two[:point]
        two_hald = all_two[point:]

        off_one = half_one + two_hald
        off_two = one_half + half_two

        ind_one = Individual(eval_func, allels_num, self.st, off_one)
        ind_two = Individual(eval_func, allels_num, self.st, off_two)

        ind_one.mutate()
        ind_two.mutate()
        return ind_one, ind_two

    def get_mating_pool(self, dens):
        mating_pool = []
        for i in range(len(self.individuals)):
            rand = random.random()
            selected = next(x for x in dens if x[0] > rand)[1]
            mating_pool.append(selected)

        return mating_pool

    def average(self):
        """ Finds average fitness for this population

        :return:
                (float): average fitness of population
        """
        #todo
        pass

    def best(self):
        """Finds best of population

        :return: (Individual): Individual with best fitness
        """
        #todo
        pass

    def add_rec(self,list, tail_list):
        if list:
            second_pair = list[0]
            last_existing = tail_list[-1]
            new_pair = (last_existing[0] + second_pair[0], second_pair[1])
            tail_list.append(new_pair)
            if list[1:]:
                self.add_rec(list[1:], tail_list)
        return tail_list