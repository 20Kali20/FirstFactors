# Kalina Dzierzak
from math import *

num = int(input("Enter number: "))
num_2 = num

factors = []
multiples = []
i = 2
y = 1
c = 0

while i <= num:
    if num % i == 0:
        if y != 1:
            factors.pop(-1)
            factors.append(str(i) + '^' + str(y))
            multiples[-1][1] = y
        else:
            factors.append(str(i))
            multiples.append([i, 1])
        num = num/i
        y += 1  
    else:
        i += 1
        y = 1

m = 1

for f in multiples:
    m *= (f[1] + 1)

divisors = []
z = 1
a = 1
while a <= ceil(m/2):
    if num_2 % z == 0:
        divisors.append(str(z))
        if z != num_2/z:
            divisors.append(str(int(num_2/z)))
        a += 1
    z += 1

print('Number of divisors: ', m)
print('Divisors: ', ','.join(divisors))
print('First factors: ', " * ".join(factors))
print(multiples)