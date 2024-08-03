import random
import sympy
import math

def monte_carlo(n, k):
    count = 0
    for i in range(k):
        input = []
        while(len(input) != n):
            random_num = random.randint(1, n)
            count = count + 1
            if random_num not in input: 
                input.append(random_num)
    return count / k

n10k10 = monte_carlo(10, 10)
print(n10k10)
n10k100 = monte_carlo(10, 100)
print(n10k100)
n10k1000 = monte_carlo(10, 1000)
print(n10k1000)

x = sympy.symbols('x')
def MGF_xi(n):
    answer = 1
    for i in range(1, n + 1):
        count = pow(math.e, x) * (1 - (i - 1) / n) / (1 - (pow(math.e, x) * ((i - 1) / n)))
        answer *= count
    return answer

MGF_X = MGF_xi(10)
deriv = sympy.diff(MGF_X, x)
print(deriv.subs({x:0}))