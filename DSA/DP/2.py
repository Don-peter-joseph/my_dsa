#print all subsets

value='abcd'

subsets=[]

def findsubsets(i,string):
    if i==len(value):
        subsets.append(string)
        return
    findsubsets(i+1,string+value[i])
    findsubsets(i+1,string)
    

findsubsets(0,'')
print(subsets)