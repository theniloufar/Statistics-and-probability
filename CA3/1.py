from keras.datasets import mnist
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

(_, _) , (test_images, _) = mnist.load_data()
test_images = test_images.reshape(test_images.shape[0] , -1)
test_images = test_images.astype('float32') / 255.0
autoencoder = tf.keras.models.load_model('mnist_AE.h5')
reconstructed_images = autoencoder.predict(test_images)

first = np.reshape(reconstructed_images[90], (28,28))
second = np.reshape(reconstructed_images[106], (28,28))
third = np.reshape(reconstructed_images[290], (28,28))
fourth = np.reshape(reconstructed_images[300], (28,28))
plt.imshow(first)
plt.show()
plt.imshow(second)
plt.show()
plt.imshow(third)
plt.show()
plt.imshow(fourth)
plt.show()

def calculate_MSE(pre, post):
    MSE = []
    for i in range(len(pre)):
        temp = 0
        for j in range(len(pre[i])):
            temp = temp + ((pre[i][j] - post[i][j]) ** 2)
        temp = temp / len(pre)
        MSE.append(temp)
    return MSE

MSE = []
MSE = calculate_MSE(test_images, reconstructed_images)
plt.hist(MSE)
plt.show()

def calculate_mean(MSE):
    temp = 0
    for data in MSE:
        temp += data
    mean = temp / len(MSE)
    return mean

def calculate_Standard_deviation(MSE, mean):
    temp_variance = 0
    for data in MSE:
        temp_variance += ((data - mean) ** 2)
    variance = temp_variance / len(MSE)
    Standard_deviation = sqrt(temp_variance) 
    return Standard_deviation

mean = calculate_mean(MSE)
Standard_deviation = calculate_Standard_deviation(MSE, mean)
ks_statistic, p_value = stats.kstest(MSE, cdf='norm', args= (mean, Standard_deviation))
print(ks_statistic, p_value)