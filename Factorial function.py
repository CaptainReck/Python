def fact(k):
    f=1
    for i in range(1,k+1,1):
        f=f*i
    return f
__builtins__.fact=fact
import re
__builtins__.re=re
