x='aggtab'
y='gxtxayb'

# x="acrs"
# y="abcdsf"

#question: find the length of the shortest supersequence    
#output :7 shortest supersequence is abcrdsf 

table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0 or j==0:
            table[i][j]=0

for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=1+table[i-1][j-1]
        else:
            table[i][j]=max(table[i][j-1],table[i-1][j])

# print(table)
common=table[len(y)][len(x)]
sslength=len(x)+len(y)-common
print(sslength)