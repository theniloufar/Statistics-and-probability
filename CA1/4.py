import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm , poisson

NumOfAccidents = 7072 #n
prob = 0.45 #p
var = 41.84 
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