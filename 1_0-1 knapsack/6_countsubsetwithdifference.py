#count the no of subset with given difference

arr=[1,1,2,3]
diff=3

#solution

#s1+s2=total sum
#s1=s2+3
#s2+s2+3=total sum
#2s2+3=totalsum

from math import ceil
total=sum(arr)

if (total-diff)%2!=0:
    print(0)
    exit(0)

target=(total-diff)//2
table=[[-1]*(target+1) for _ in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(target+1):
        if i==0 and j!=0:
            table[i][j]= 0
        if j==0:
            table[i][j]= 1

for i in range(1,len(arr)+1):
    for j in range(1,target+1):
        if(j>=arr[i-1]):
            table[i][j]=table[i-1][j-arr[i-1]]+table[i-1][j]
        else:
            table[i][j]=table[i-1][j]

print(table[len(arr)][target])