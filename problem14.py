# PROJECT EULER PROBLEM 14
# With respect to given chain rule what is the starting number of longest chain under one million
# https://projecteuler.net/problem=14
def chain_lenght (n):
    i=1
    y=n
    while n!=1:
        i+=1
        if n%2==0:
            n=n//2

        else:
            n=3*n+1


    return (i,y)

liste=[]
maxlenght=0
print(chain_lenght(13))

for i in range (2,1000000):
    print(chain_lenght(i))

    if maxlenght<chain_lenght(i)[0]:
        maxlenght=chain_lenght(i)[0]
        liste.append([maxlenght,i])
print(liste)
print(chain_lenght(i)[0])


