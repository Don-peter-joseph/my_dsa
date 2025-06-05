x="T | F & T ^ F"

#question . The string can only contain True-'T',False -'F', or &,|,^ operators.
#find the no of ways the brackets can be applied so that the answer will be True.

def solve(arr,i,j):
    if i==j:
        return x[i]
    for k in range(i,j):
        temp=solve(arr,i,k)+x[k+1]+solve(arr,k+2,j)
ans=solve(x,0,len(x)-1)
print(ans)

#not found solution for this