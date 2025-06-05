#divide an array into two such that sum of both subset are the same.return true if it is possible.else return false.
#using table method
arr=[1,2,2,7,4]
arrsum=sum(arr)

table=[[-1]*((arrsum//2)+1) for i in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(arrsum//2+1):
        if(j==0):
            table[i][j]=True
        if(i==0):
            table[i][j]=False

# print(table)
def equalsumpartition(arr,sum):
    if(arrsum%2!=0):
        return False
    for i in range(1,len(arr)+1):
        for j in range(1,sum+1):
            if(arr[i-1]<=j):
                table[i][j]=max(table[i-1][j-arr[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    return table[len(arr)][sum//2]

value=equalsumpartition(arr,arrsum//2)
print(value)
# print(arrsum//2)