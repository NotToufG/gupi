from math import sqrt
from .variance import variance
def stddev(lst):
    return sqrt(variance(lst))