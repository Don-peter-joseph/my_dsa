"""count of subsets of a given sum"""

arr=[2,3,5,6,8,10]
sum=10

table=[[-1]*(sum+1) for _ in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(sum+1):
        if i==0 and j!=0:
            table[i][j]=0
        if j==0:
            table[i][j]=1

for i in range(1,len(arr)+1):
    for j in range(1,sum+1):
        if j>=arr[i-1]:
            table[i][j]=table[i-1][j-arr[i-1]]+table[i-1][j]
        else:
            table[i][j]=table[i-1][j]

print(table[len(arr)][sum])
# print(table)

