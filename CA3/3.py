import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import random 
import scipy.stats as stats 

def initialize_random_seeds(seed_value): 
    random.seed(seed_value) 
    np.random.seed(seed_value) 
    initialize_random_seeds(810109203) 
    
data_frame = pd.read_csv('FIFA2020.csv', encoding="ISO-8859-1") 
    
def replace_nan_with_mean(column_name):
    mean_value = data_frame[column_name].mean() 
    data_frame[column_name].fillna(mean_value, inplace=True) 

replace_nan_with_mean('pace') 
replace_nan_with_mean('dribbling') 
data_frame.boxplot(column='age') 
plt.show() 
age_stats = data_frame['age'].agg(['min', 'max', 'quantile']) 
print(age_stats['min'], age_stats['max'], age_stats.quantile(0.25), age_stats.quantile(0.5), age_stats.quantile(0.75)) 

sample_size = 2000 
weights_sample = random.choices(data_frame['weight'], k=sample_size) 
sample_mean = np.mean(weights_sample) 
sample_variance = np.var(weights_sample) 

print(sample_mean, sample_variance, np.sqrt(sample_variance)) 
normal_dist_sample = np.random.normal(sample_mean, np.sqrt(sample_variance), sample_size) 

plt.scatter(normal_dist_sample, weights_sample) 
plt.plot([min(weights_sample), max(weights_sample)], [min(weights_sample), max(weights_sample)]) 
plt.show() 
shapiro_stat, shapiro_p = stats.shapiro(weights_sample) 
print(shapiro_p)