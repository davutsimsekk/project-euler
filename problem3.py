# PROJECT EULER PROBLEM 3
# https://projecteuler.net/problem=3
# WHAT IS THE LARGEST PRIME FACTOR OF A NUMBER

our_number = int(input("PLEASE ENTER A NUMBER: "))
prime_factors = []
while our_number % 2 == 0:
    our_number = our_number / 2

# FIRST TWO'S MULTIPLIERS HAVE BEEN ELIMINATED SO THAT WE CAN JUMP TWO BY TWO IN THE STATEMENT BELOW

for i in range(3, int(our_number ** 0.5)+1, 2):
    if not our_number % i:
        prime_factors.append(i)
        our_number = our_number / i
# WE HAVE TO DIVIDE OUR NUMBER BY MULTIPLIER SO WE ELIMINATE NON-PRIME NUMBERS

print(max(prime_factors))
