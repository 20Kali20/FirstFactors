from math import *

num = int(input("Enter number: "))

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

while q <= (len(factors) - 1):
    n = factors.count(factors[q])
    if n != 1:
        factors_2.append(str(factors[q]) + '^' + str(n))
    else:
        factors_2.append(str(factors[q]))
    q += n

print(" * ".join(factors_2))