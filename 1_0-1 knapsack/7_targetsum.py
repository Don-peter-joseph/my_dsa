#find the count for target sum
#eg ar=[1,1,2,3], target =3
# assign sign before each element
#  -1-1+2+3 =3                 =>output should be the count of such combination

#solution
#here (-1,-1) (2,3,) is subset .ie (2,3)-(1,1). This is actually to find the count of subset with given difference. same as last one. only the question is different.

arr=[1,1,2,3]
sum=1

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