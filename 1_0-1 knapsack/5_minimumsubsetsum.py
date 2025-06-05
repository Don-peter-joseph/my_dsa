#minimum subset sum d/f - The minimum difference that can be made after partitioning into two

arr=[1,6,11,5,3]

#solution starts
from math import ceil

diff=sum(arr)

table=[[-1]*(diff+1) for _ in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(diff+1):
        if i==0 and j!=0:
            table[i][j]=False
        if j==0:
            table[i][j]=True


for i in range(1,len(arr)+1):
    for j in range(1,diff+1):
        if diff>=arr[i-1]:
            table[i][j]=max(table[i-1][j-arr[i-1]],table[i-1][j])
        else:
            table[i][j]=table[i-1][j]

print(table[len(arr)][diff])

#upto here it same as subset sum.
#we only need to see the closest sum to (diff/2) or range-2s1 to get the output


minimum=diff
for j in range(0,ceil((diff+1)/2)):
    if table[len(arr)][j]==True:
        minimum=min(minimum,diff -(2*j))
    
print(minimum)