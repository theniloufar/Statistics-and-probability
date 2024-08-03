import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm , poisson

NumOfAccidents = 250 #n
prob = 0.008 #p
var = 1.984  
list = np.array(range(NumOfAccidents))
mu = NumOfAccidents * prob

def bin():
    x = np.array(range(NumOfAccidents))
    y = binom.pmf(list , NumOfAccidents , prob)
    plt.plot(x , y)

def poi():
    x = np.array(range(NumOfAccidents))
    y = poisson.pmf(list , mu)
    plt.plot(x , y)

def N():
    x = np.array(range(NumOfAccidents))
    y = norm.pdf(list , mu , var)
    plt.plot(x , y)

bin()
poi()
N()
plt.show()