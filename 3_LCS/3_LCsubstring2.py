x="adfasdfsc"
y="abcawefsdfc"

#question: print longest common substring
#output :abc
maxstring=""
table=[[-1]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)+1):
    for j in range(len(x)+1):
        if i==0 or j==0:
            table[i][j]=""

for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1]==y[i-1]:
            table[i][j]=max(x[j-1]+table[i-1][j-1],table[i-1][j],table[i][j-1])
            if len(table[i][j])>=len(maxstring):
                maxstring=table[i][j]
        else:
            table[i][j]=""
print(maxstring[::-1])
print(table)