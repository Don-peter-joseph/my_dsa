arr=[10, 20, 30, 40, 30 ]

#question:find the cost of matrix multiplication

#solution:
table=[[-1]*100 for _ in range(100)]

def mcm(arr,i,j):
    if i>=j:
        return 0
    if table[i][j]!=-1:
        return table[i][j]
    min=999999
    for k in range(i,j):
        temp=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        if temp<min:
            min=temp
            table[i][j]=min
    return min

ans=mcm(arr,1,len(arr)-1)
print(ans)