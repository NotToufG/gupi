from .mean import mean
def variance(lst):
    m=mean(lst)
    return sum((x-m)**2 for x in lst)/len(lst)