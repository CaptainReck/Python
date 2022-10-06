n=int(input(" "))
def fact(k):
    f=1
    for i in range(1,k+1,1):
        f=f*i
    return f
sum=n
for i in range(2,n+1,1):
    sum=sum+(n**i/fact(2*i-1))
print(sum)    
