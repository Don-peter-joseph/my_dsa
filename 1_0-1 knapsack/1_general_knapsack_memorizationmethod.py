#normal 0/1 knapsack using only memorization method

wt=[2,4,5,2,5]
val=[3,2,4,3,4]
w=8

table=[[-1]*10]*10
# print(table)
def knapsack(wt,val,w,n):
    if(w==0 or n==0):
        return 0
    if(table[n][w]!=-1):
        return table[n][w]
    if(wt[n-1]<=w):
        table[n][w]= max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        return table[n][w]
    else:
        table[n][w]=knapsack(wt,val,w,n-1)
        return table[n][w]
    
output=knapsack(wt,val,w,len(wt))
print(output)