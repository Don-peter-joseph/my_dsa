#normal 0/1 knapsack using only table only method


wt=[2,4,5,3,5]
val=[3,2,4,3,4]
w=8

table=[[-1]*(w+1) for _ in range(len(wt) + 1)]
for i in range(len(wt)+1):
    for j in range(w+1):
        if(i==0 or j==0):
            table[i][j]=0
# print(table)
def knapsack(wt, val, w, n):
    for i in range(n+1):
        for j in range(w+1):
            if(wt[i-1]<=j):
                table[i][j]=max(val[i-1]+table[i-1][j-wt[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table[i][j]

output=knapsack(wt,val,w,len(wt))
print(output)
print(table)