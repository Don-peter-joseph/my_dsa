#count the no of ways in which the coins can be selected to get the sum.coins are unlimited

coins=[1,2,3]
sum=5

table=[[-1]*(sum+1) for _ in range(len(coins)+1)]

for i in range(len(coins)+1):
    for j in range(sum+1):
        if i==0 and j!=0:
            table[i][j]=0
        if j==0:
            table[i][j]=1


for i in range(1,len(coins)+1):
    for j in range(1,sum+1):
        if coins[i-1]<=j:
            table[i][j]=table[i][j-coins[i-1]]+table[i-1][j]
        else:
            table[i][j]=table[i-1][j]
            
print(table[len(coins)][sum])