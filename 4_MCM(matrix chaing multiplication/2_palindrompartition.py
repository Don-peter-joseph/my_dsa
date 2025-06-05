x='tararus'

#find the minimum no partitions to make the partioned strings as palindrome
#eg = 'peter' -> p | ete | r   . so 2 partitions

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
    min=99
    for k in range(i,j):
        temp=palindrompartition(x,i,k)+palindrompartition(x,k+1,j)+1
        if min>temp:
            min=temp
    return min

ans=palindrompartition(x,0,len(x)-1)
print(ans)