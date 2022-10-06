n=int(input("# "))
sum=0;x=n;d=0
while x!=0:
    r=x%10
    d=r**3+d
    x=x//10
if(n==d):
    print("arm")
else:
    print("n")
    
