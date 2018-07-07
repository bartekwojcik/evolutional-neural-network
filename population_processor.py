from individual import Individual
from population import Population

class Population_processor(object):
    def __init__(self, nn_param_choices, retain=0.4,
                 random_select=0.1, mutate_chance=0.02):
        """Create an optimizer.

        Args:
            nn_param_choices (dict): Possible network paremters
            retain (float): Percentage of population to retain after each generation
            random_select (float): Probability of a rejected network remaining in the population
            mutate_chance (float): Probability a network chromosome will be randomly mutated

        """
        self.mutate_chance = mutate_chance
        self.random_select = random_select
        self.retain = retain
        self.nn_param_choices = nn_param_choices

    def create_population(self, popsize):
        """Create a population of random networks.

        Args:
            count (int): population size

        Returns:
            Population: Population of network objects

        """
        pop = []
        for _ in range(0, popsize):
            # Create a random network.
            # todo init paramters
            network = Individual(self.nn_param_choices)
            network.create_random()
            # Add the network to our population.
            pop.append(network)

        return Population(pop)

    def evolve(self, pop):
        """Evolve a population of networks.

        Args:
            pop (list): A list of network parameters

        Returns:
            (list): The evolved population of networks

        """
        #todo completly rewrite
        # Get scores for each network.
        graded = [(self.fitness(network), network) for network in pop]

        # Sort on the scores.
        graded = [x[1] for x in sorted(graded, key=lambda x: x[0], reverse=True)]

        # Get the number we want to keep for the next gen.
        retain_length = int(len(graded) * self.retain)

        # The parents are every network we want to keep.
        parents = graded[:retain_length]

        # For those we aren't keeping, randomly keep some anyway.
        for individual in graded[retain_length:]:
            if self.random_select > random.random():
                parents.append(individual)

        # Now find out how many spots we have left to fill.
        parents_length = len(parents)
        desired_length = len(pop) - parents_length
        children = []

        # Add children, which are bred from two remaining networks.
        while len(children) < desired_length:

            # Get a random mom and dad.
            male = random.randint(0, parents_length - 1)
            female = random.randint(0, parents_length - 1)

            # Assuming they aren't the same network...
            if male != female:
                male = parents[male]
                female = parents[female]

                # Breed them.
                babies = self.breed(male, female)

                # Add the children one at a time.
                for baby in babies:
                    # Don't grow larger than desired length.
                    if len(children) < desired_length:
                        children.append(baby)

        parents.extend(children)

        return parents