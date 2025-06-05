#divide an array into two such that sum of both subset are the same.return true if it is possible.else return false.

arr=[1,2,2,7]
arrsum=sum(arr)

def equalpartition(arr,n,sum):
    if(arrsum%2!=0):
        return False
    else:
        if(sum==0):
            return True
        if(n==0 and sum!=0):
            return False
        if(arr[n]<=sum):
            res=max(equalpartition(arr,n-1,sum-arr[n]),equalpartition(arr,n-1,sum))
            return res
        else:
            res=equalpartition(arr,n-1,sum)
            return res

value=equalpartition(arr,len(arr)-1,arrsum/2)
print(value)
