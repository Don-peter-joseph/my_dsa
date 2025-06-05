people=10
count=0

table=[-1]*100

def comb(n):
    global count
    count+=1
    if n==1 or n==0:
        return 1
    if table[n]!=-1:
        return table[n]
    
    table[n]=comb(n-1)+(n-1)*comb(n-2)
    return table[n]
    

ans=comb(people)
print(ans,count)

