a=54
b=36;i=1;f=1
while i<a and i<b:
    af=a%i
    bf=b%i
    if af==0 and bf==0:
        f=i
    i=i+1    
print(f)    
