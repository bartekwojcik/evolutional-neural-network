from optproblems import *
class FunctionProvider():

    def __init__(self, function):
        self.Problem = Problem(function)
    def calc_funct(self, x, y):
        solution = Individual([x,y])
        self.Problem.evaluate(solution)
        #returning negative value because my algorithm treats the highest value as the best
        return -1 * solution.objective_values
    def get_range(self):
        function = self.Problem.objective_function
        return function.max_bounds, function.min_bounds





# from math import *
# class MatyasFunctionProvider():
#     def calc_funct(self,x,y):
#         return -1 * (0.26 * (x ** 2 + y ** 2) - 0.48 * x * y)
#     def get_range(self):
#         return [(-10,10),
#                 (-10,10)]
#
#
# class EasomFunctionProvider():
#     def calc_funct(self,x,y):
#         return -1 * (- cos(x) * cos(y) * exp(-( ((x - pi)**2) + ((y - pi)**2))))
#     def get_range(self):
#         return [(-100,100),
#                 (-100,100)]
#
#
# class HimmelblausFunctionProvider():
#     def calc_funct(self,x,y):
#         return -1 * ( ((x**2 + y - 11)**2) + (x+y**2 -7)**2  )
#     def get_range(self):
#         return [(-5,5),
#                 (-5,5)]
