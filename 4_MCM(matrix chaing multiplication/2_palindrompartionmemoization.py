x='tararus'

#find the minimum no partitions to make the partioned strings as palindrome
#eg = 'peter' -> p | ete | r   . so 2 partitions
#memoization method

table=[[-1]*(len(x)+1) for _ in range(len(x)+1)]

def ispalindrome(x,i,j):
    val=x[i:j+1]
    rev=val[::-1]
    if rev==val:
        return True
    return False

def palindrompartition(x,i,j):
    if i>=j:
        return 0
    if ispalindrome(x,i,j):
        return 0
    if table[i][j]!=-1:
        return table[i][j]
    min=99
    for k in range(i,j):
        #optimized solution below

        # if table[i][k]!=-1:
        #     left=table[i][k]
        # else:
        #     left=palindrompartition(x,i,k)
        #     table[i][k]=left
        # if table[k+1][j]!=-1:
        #     right=table[k+1][j]
        # else:
        #     right=palindrompartition(x,k+1,j)
        #     table[k+1][j]=right
        # temp=left+right+1
        temp=palindrompartition(x,i,k)+palindrompartition(x,k+1,j)+1
        if min>temp:
            min=temp
            table[i][j]=min
    return min

ans=palindrompartition(x,0,len(x)-1)
print(ans)