n=int(input("enter n"))
arr=list(map(int,input().split()))
def funct(input1,input2):
    rank=[]
    for i in range(0,input1,1):
        rank.append([input2[x]>input2[i] for x in range(0,i)].count(True))                
    return rank       
print(funct(n,arr))
