class MatyasFunctionProvider():
    def calc_funct(self,x,y):
        return 0.26 * (x ^ 2 + y ^ 2) - 0.48 * x * y
    def get_range(self):
        return [(-10,10),
                (-10,10)]
