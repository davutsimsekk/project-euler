# PROJECT EULER PROBLEM 7
# What is the 1001'st prime number?
# https://projecteuler.net/problem=7
counter = 0
i = 2


def is_it_prime(x):
    is_prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            x = x / i

    return is_prime


while True:
    if is_it_prime(i):
        counter += 1
        print(counter, end=" ")
        print(i)
        if counter == 10001:
            break
    i += 1
print(counter,"th prime number is", i)
