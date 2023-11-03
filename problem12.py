# PROJECT EULER PROBLEM 12
# What is the value of the first triangle number to have over five hundred divisors?
# https://projecteuler.net/problem=12
n = 1
k = (n * (n + 1)) // 2


def number_of_divisor(x):
    number = 0
    for i in range(1, int((x ** 0.5)) + 1):
        if not x % i:
            number += 2
    return number


while number_of_divisor(k) < 500:
    n += 1
    k = (n * (n + 1)) // 2
    print(n, k)
print(n, k)
