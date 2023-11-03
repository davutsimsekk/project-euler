# PROJECT EULER PROBLEM 10
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# https://projecteuler.net/problem=6

k = 100 * 101 // 2
result = 0
for i in range(1, 101):
    result += i * i
print(k * k - result)
