from math import sqrt
n=0
while n<2 or n>100:
    n=int(input("saisir N"))
S=0
max=0
for i in range(2,n+1):
    est_premier='true'
    for j in range(2,int(sqrt(n))+1):
        if i%j==0 and i!=j:
            est_premier='false'
        if est_premier=false and i==n:
            print(n,'non premier',j)
            break
        if est_premier:
            if n==i:
                print(n,'est premier')
            print(i)
            S+=i
            if max < i:
                max=i
    print('somme des nbres premiers :',S)
    print('max premiers :',max)