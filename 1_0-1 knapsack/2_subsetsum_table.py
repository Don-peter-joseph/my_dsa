#Find if there exists a subset whose sum matches the given sum using only table,no recursion. 
arr=[3,3,4,6,2,10]
sum=28

table=[[-1]*(sum+1) for _ in range(len(arr)+1)]
for i in range(len(arr)+1):
    for j in range(sum+1):
        if(j==0):
            table[i][j]=True
        if(i==0 and j!=0):
            table[i][j]=False

# print(table)
def subsetsum(arr,sum,n):
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if(arr[i-1]<=j):
                table[i][j]=max(table[i-1][j-arr[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table[len(arr)][sum]
output=subsetsum(arr,sum,len(arr))
print(output)
# print(table)