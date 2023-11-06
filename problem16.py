# PROJECT EULER PROBLEM 16
# What is the sum of the digits of 2^1000 the number
# https://projecteuler.net/problem=16
c=2**1000
list_for_digits=[]
for i in str(c):
    list_for_digits.append(int(i))

print(list_for_digits)
print("Sum of all digits are:", sum(list_for_digits))