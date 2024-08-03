import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.metrics import r2_score 

def multiply_elements(list1, list2): 
    return [a * b for a, b in zip(list1, list2)] 

def linear_regression_analysis(x_data, y_data): 
    n = len(x_data) 
    x_squared = multiply_elements(x_data, x_data) 
    y_squared = multiply_elements(y_data, y_data) 
    xy_product = multiply_elements(x_data, y_data) 

    sum_x = sum(x_data) 
    sum_y = sum(y_data) 
    sum_x_squared = sum(x_squared) 
    sum_y_squared = sum(y_squared) 
    sum_xy = sum(xy_product) 

    regression_slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2) 
    regression_intercept = (sum_y - regression_slope * sum_x) / n 

    r2_value = ((n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2)))**2 
    return regression_slope, regression_intercept, r2_value 

def plot_regression_line(x, y, slope, intercept): 
    x_vals = np.linspace(min(x) - 1, max(x) + 1, 100) 
    y_vals = slope * x_vals + intercept 
    plt.plot(x_vals, y_vals) 
    plt.scatter(x, y) 
    plt.show() 

def print_regression_details(slope, intercept, r2): 
    print("Slope:", slope) 
    print("Intercept:", intercept) 
    print("R^2 Value:", r2) 

x = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5] 
y = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5] 
slope, intercept, r2 = linear_regression_analysis(x, y) 
print_regression_details(slope, intercept, r2) 
plot_regression_line(x, y, slope, intercept)