import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

mu = 80
std = 12 
var = std * std

def a(): #الف
    result = norm.ppf(0.9 , mu , std)
    return result
def b(): #ب
    result= norm.ppf(0.75 , mu , std) - norm.ppf(0.5 , mu , std)
    return result
def c(): #ج
    result = norm.cdf(90 , mu , var) - norm.cdf(80 , mu , var)
    return result

print(a())
print(b())
print(c())