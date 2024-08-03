import choice 
import numpy as np 
import matplotlib.pyplot as plt

samples = 5000
trials = 500
p_value = 101
matrix = []

def mybinomial(m , n , prob):
    matrix = np.random.choice([1 , 0] , p = [prob , 1 - prob], size = (m * n))
    matrix = matrix.reshape(m , n)
    return np.sum(matrix , axis = 1)

def practical_exp():
    x = np.array(range(p_value))
    y = []
    for p in range(p_value):
        y.append(np.array(np.sum(np.sum(mybinomial(samples , trials , p * 0.01)))/samples))
    plt.plot(x , y)

def theoretical_exp():
    x = np.array(range(p_value))
    y = []
    for p in range(p_value):
        y.append(np.array((trials * p * 0.01)))
    plt.plot(x , y)

def practical_var():
    x = np.array(range(p_value))
    y = []
    for p in range(p_value):
        y.append(np.array(np.var(mybinomial(samples, trials, p * 0.01))))
    plt.plot(x , y)

def theoretical_var():
    x = np.array(range(p_value))
    y = []
    for p in range(p_value):
        y.append(np.array(trials * (p * 0.01) * (1 - (p * 0.01))))
    plt.plot(x , y)

theoretical_exp()
practical_exp()
plt.show()
theoretical_var()
practical_var()
plt.show()