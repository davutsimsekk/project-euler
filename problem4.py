# PROJECT EULER PROBLEM 4
# Find the largest palindrome made from the product of two 3-digit numbers.
# https://projecteuler.net/problem=4
number=""
liste=[]
for i in range (100,1000):
    for a in range(100,1000):
        number= str(i*a)

        if number==number[::-1]:
            liste.append(i*a)

print(liste)
print(max(liste))