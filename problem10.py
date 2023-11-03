# PROJECT EULER PROBLEM 10
# Find the sum of all the primes below two million.
# https://projecteuler.net/problem=10

counter = 1
i = 3
result = 2


def is_it_prime(number):                                #FUNCTION THAT RETURNS WHETHER IT IS PRIME OR NOT
    is_prime = True
    if number%2==0:
        is_prime=False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                number = number / i

    return is_prime


while i < 2e6:

    if is_it_prime(i):
        counter += 1
        print(counter, end=" ")

        result = i + result
        print(i, result)

    i += 2
print("{}th prime number , last prime number {}, total until last prime number {} ".format(counter, i-1, result))
