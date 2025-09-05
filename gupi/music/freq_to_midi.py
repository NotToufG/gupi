import math
def freq_to_midi(freq):
    return round(69+12*math.log2(freq/440))