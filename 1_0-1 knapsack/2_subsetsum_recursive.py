#Find if there exists a subset whose sum matches the given sum.

arr=[3,3,4,6,2,10]
sum=11

def subsetsum(arr,sum,n):
    if(sum==0):
        return True
    if(n==0 and sum!=0):
        return False
    if(arr[n-1]<=sum):
        return max(subsetsum(arr,sum-arr[n-1],n-1),subsetsum(arr,sum,n-1))
    else:
        return subsetsum(arr,sum,n-1)

output=subsetsum(arr,sum,len(arr))
print(output)