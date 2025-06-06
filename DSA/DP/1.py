#find longest increasing subsequence's length
#eg [4,2,7,4,3,5] ans: longest increasing subsequence is [2,3,5] , therefore len is 3

# arr=[4,2,7,4,8,9,3,5]
arr = [10, 22, 9, 33, 21, 50, 41, 60]

total=0
table=[-1 for i in range(len(arr)+1)]

def findlongest(count,i,prev):
    global total
    total+=1
    if i==len(arr):
        return count
    if table[i]!=-1:
        return table[i]
    if arr[i]>=prev:
        table[i]=max(findlongest(count+1,i+1,arr[i]),findlongest(count,i+1,prev))
        return table[i]
    else:
        table[i]=findlongest(count,i+1,prev)
        return table[i]
    
ans=findlongest(0,0,0)
print(ans,total)