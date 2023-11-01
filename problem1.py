# PROJECT EULER PROBLEM 1
# https://projecteuler.net/problem=1


# FIRST SOLUTION
# result = 0
# for i in range(1000):
#     if i%3==0 or i%5==0:
#         result+=i

# SECOND SOLUTION
def f(x, m):
    x -= 1
    k = (x - x % m) / m
    return int(m * k * (k + 1) / 2)


def lcm(x: int, y: int):
    return x * y / gcd(x, y)


def gcd(x: int, y: int):
    gcd_result = 1

    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd_result = i
    return gcd_result


def calculate(x, y, z):
    return f(z, x) + f(z, y) - f(z, lcm(x, y))

# Multiples of x and y
# Find the sum of all the multiples of X or Y below Z

print(calculate(3, 5, 1000))


