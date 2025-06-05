#normal 0/1 knapsack using only recursive method

wt=[2,4,5,2,5]
val=[3,2,4,3,4]
w=8

def knapsack(wt,val,w,n):
    if(w==0 or n==0):
        return 0
    if(wt[n-1]<=w):
        return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
    elif(wt[n-1]>w):
        return knapsack(wt,val,w,n-1)
output=knapsack(wt,val,w,len(wt))
print(output)