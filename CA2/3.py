import random
import numpy
import pandas
import matplotlib.pyplot as plt

array_size = 28
data = pandas.read_csv(r"C:\Users\NanoCamp\Downloads\CA2\digits.csv")

data201 = data.loc[200]
data202 = data.loc[201]
data = data.drop(201)
data = data.drop(200)

for i in range(len(data)):
    for j in range(1, len(data.loc[i])):
        if (data.iat[i, j] < 128):
            data.iat[i, j] = 0
        else:
            data.iat[i, j] = 1

index = random.randint(0, len(data) - 1)
row = data.loc[index]
row = numpy.reshape(row[1:], (array_size , array_size))
plt.imshow(row)
plt.show()