import random
import numpy as np

def blend_crossover(x1,x2,alpha):
    """Performs blend crossover with giver alpha over given x1 and x2

        :params: x1,x2, alpha: float numbers

        :returns: (float, float)
    """
    smaller = x1 if x1<x2 else x2
    bigger = x1 if x1>x2 else x2
    substraction = bigger - smaller
    floor = smaller - alpha * substraction
    ceil = bigger + alpha * substraction
    y1 = random.uniform(floor, ceil)
    y2 = random.uniform(floor, ceil)

    return y1,y2


def simulated_binary_crossover(p1,p2,n):
    """
    Simulated Binary Crossover

    :param p1: array NxD
    :param p2: array NxD
    :param n: control parameter
    :return: two arrays NxD
    """

    #todo now i assume that p1 and p2 has the same size, what if they are diffrent?

    size1 = p1.shape
    size2 = p2.shape

    if size1 != size2:
        raise ValueError("oops, sizes are not the same")

    u = np.random.rand(size1[0],size1[1])
    beta = np.where(u<=0.5,(2*u)**(n+1), (2*(1-u))**(-1/(n+1)))
    c1 = 0.5*(p1+p2)+0.5*beta*(p1-p2)
    c2 = 0.5*(p2+p1)+0.5*beta*(p2-p1)

    return c1,c2




