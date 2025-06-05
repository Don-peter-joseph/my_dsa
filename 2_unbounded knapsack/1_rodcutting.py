#cut the rod such that profit can be maximised. Return the maximum profit.'n' is the lenght of the rod

length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
n=8

table=[[-1]*(n+1) for _ in range(len(length)+1)]

for i in range(len(length)+1):
    for j in range(n+1):
        if i==0:
            table[i][j]=0
        if j==0:
            table[i][j]=0

for i in range(1,len(length)+1):
    for j in range(1,n+1):
        if length[i-1]<=j:
            table[i][j]=max(price[i-1]+table[i][j-length[i-1]],table[i-1][j])
        else:
            table[i][j]=table[i-1][j]

print(table[len(length)][n])

print(table)