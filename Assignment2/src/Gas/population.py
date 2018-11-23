from collections import OrderedDict
from src.Gas.individual import Individual
from src.Gas.mutators import *
from src.utils import My_Dict
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
        std_x,std_y = self.get_standard_dev(mating_pool)
        random.shuffle(mating_pool)
        offspring_list = []
        for i in range(0, len(mating_pool), 2):
            one = mating_pool[i]
            two = mating_pool[i + 1]
            off_one, off_two = self.crossover(one, two,self.mutations_params,std_x,std_y)

            offspring_list.append(off_one)
            offspring_list.append(off_two)
        return offspring_list

    def get_standard_dev(self,mating_pool):
        xs = [ind.x for ind in mating_pool]
        ys = [ind.y for ind in mating_pool]

        return np.array(xs).std(),np.array(ys).std()

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

        mating_pool += parents

        children = self.breed_mating_pool(mating_pool)

        return Population(children,self.popsize, self.mutations_params)

    def crossover(self, mother, father, mutations_params,std_x, std_y):
        """Make two children as parts of their parents.

        Args:
            mother (dict): Network (Individuals) parameters
            father (dict): Network (Individuals) parameters

        Returns:
            (tuple): Two Individuals objects

        """
        y1_d = My_Dict()
        y2_d = My_Dict()

        y1_d.range_array = mother.range_array
        y2_d.range_array = father.range_array

        x1,x2 = blend_crossover(mother.x,father.x,mutations_params.alpha_blend)
        y1,y2 = blend_crossover(mother.y,father.y,mutations_params.alpha_blend)

        y1_d.x = x1
        y1_d.y = y1

        y2_d.x = x2
        y2_d.y = y2

        y1 = Individual(chromosomes=y1_d,
                        chrom_provider=mother.chrom_provider)
        y2 = Individual(chromosomes=y2_d,
                        chrom_provider=mother.chrom_provider)

        y1.mutate(mutations_params.mutate_chance,std_x, std_y)
        y2.mutate(mutations_params.mutate_chance,std_x, std_y)

        y1.keep_in_range()
        y2.keep_in_range()
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