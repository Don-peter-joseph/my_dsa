x="abcdghtesdf"
y="abedfhre"

#question: Find the length of longest common subsequenc
#output :5 ,lcs= abdhe

def rec(x,y,m,n):
    if len(x)==0 or len(y)==0:
        return 0
    if x[m]==y[n]:
        return 1+rec(x[:-1],y[:-1],m-1,n-1)
    else:
        return max(rec(x[:-1],y,m-1,n),rec(x,y[:-1],m,n-1))
    
value=rec(x,y,len(x)-1,len(y)-1)
print(value)