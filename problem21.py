# PROJECT EULER PROBLEM 21
# Evaluate the sum of all the amicable numbers under 10000.
# https://projecteuler.net/problem=21
def d(n):
    total=0
    result=0
    for i in range(1, int((n/2)+1)):
        if n%i==0:
            total+=i
    return total


result=0
for i in range(1,10001):
    if d(d(i))==i and d(i)!=i:
        result+=i

print(result)

#I don't know recursive function so this is what i can do most.

