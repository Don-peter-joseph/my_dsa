#count the no of way brackets can be arranged

val=4
recursive_calls=0
stringlength=(val*2)
ways=0 


def check_ways(i,flag,ways):
    global recursive_calls,stringlength
    recursive_calls+=1
    # print(i,stringlength)
    if i==stringlength and flag==0:
        ways+=1
        return ways
    if flag==-1 or i==stringlength:
        return ways
    ways=check_ways(i+1,flag+1,ways)
    ways=check_ways(i+1,flag-1,ways)

    return ways
ans=check_ways(0,0,0)
print(ans,recursive_calls)