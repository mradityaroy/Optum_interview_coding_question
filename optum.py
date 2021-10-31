n=int(input("enter n"))
arr=[]
for i in range(n):
    inp=int(input("enter"))
    arr.append(inp)
def funct(input1,input2):
    rank=[]
    for i in range(0,input1,1):
        if arr[i]>=arr[i-1]:
            rank.append(0)
        else:
            rank.append([input2[x]>input2[i] for x in range(0,i)].count(True))
                
    return rank
        
print(funct(n,arr))
