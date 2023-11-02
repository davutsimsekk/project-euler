# PROJECT EULER PROBLEM 3
# https://projecteuler.net/problem=3
# Sum of fibonacci sequence whose values do not exceed given number

x = 1
y = 1
z=int(input("Pick a number: "))
result = 0
while y < z:

    x, y = y, x + y

    if not y % 2:
        result = result + y
print(result)
