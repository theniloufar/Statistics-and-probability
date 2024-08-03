import matplotlib.pyplot as plt
import pandas
import scipy.stats
import numpy

tarbiat_data = pandas.read_csv(r"C:\Users\NanoCamp\Downloads\CA2\Tarbiat.csv")
metro = list(tarbiat_data.loc[:, "metro"])
BRT = list(tarbiat_data.loc[:, "BRT"])
plt.hist(metro)
plt.hist(BRT)
plt.show() #part2

X = sum(metro) / len(metro) #lambda X
Y = sum(BRT) / len(BRT) #lambda Y
Z = X + Y #lambda Z

poisson_X = scipy.stats.poisson.pmf(list(range(0, 20)), X)
poisson_Z = scipy.stats.poisson.pmf(list(range(0, 20)), Z)
metro_BRT  = numpy.array(metro) + numpy.array(BRT)
n = 8
p = X / Z
w_binomial = scipy.stats.binom.pmf(list(range(0, 25)), n, p)

metro_BRT_index = []
for i in range(len(metro_BRT)):
    if metro_BRT[i] == 8:
        metro_BRT_index.append(i)

metro_index = []
for i in range(len(metro)):
    if i in metro_BRT_index: 
        metro_index.append(metro[i])

plt.hist(metro, density=True)
plt.plot(poisson_X)
plt.show() #part4

plt.plot(poisson_Z)
plt.hist(metro + BRT, density=True)
plt.show() #part5

plt.hist(metro_index, density=True)
plt.plot(w_binomial)
plt.show() #part7&8