arr=[10, 20, 30, 40, 30 ]

#question:find the cost of matrix multiplication

#solution:

def mcm(arr,i,j):
    if i>=j:
        return 0
    min=9999999999
    for k in range(i,j):
        temp=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
        # print(temp)
        if temp<min:
            min=temp
    return min

ans=mcm(arr,1,len(arr)-1)
print(ans)