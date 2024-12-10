import math as m

def logarithm_first(x: float) -> float:
    return m.log(x+3) + m.exp(x-2) - m.log10(m.exp(x-3)) / 2*x-1

def logarithm_second(x: float) -> float:
    return m.log(m.factorial(x)) + m.pow(logarithm_second(x + 2), 1 / 4) - ((1)/ m.sqrt(m.log10(x)))

def logarithm_third(x:float) -> float:
    return m.log(m.pow(x) + (1)) * m.exp(1/ (x - 1)) - (1 / (m.log(x+2)))
