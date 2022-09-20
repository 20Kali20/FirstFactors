# Kalina Dzierzak
from math import *

num = int(input("Enter number: "))
num_2 = num

factors = []
i = 2

while i <= num:
    if num % i == 0:
        factors.append(i)
        num = num/i
    else:
        i += 1

factors_2 = []
q = 0
m = 1

while q <= (len(factors) - 1):
    n = factors.count(factors[q])
    m *= (n + 1)
    if n != 1:
        factors_2.append(str(factors[q]) + '^' + str(n))
    else:
        factors_2.append(str(factors[q]))
    q += n

divisors = []
z = 1
a = 1
while a <= m/2:
    if num_2 % z == 0:
        divisors.append(str(z))
        divisors.append(str(int(num_2/z)))
        a += 1
    z += 1

print('Number of divisors: ', m)
print('Divisors: ', ','.join(divisors))
print('First factors: ', " * ".join(factors_2))