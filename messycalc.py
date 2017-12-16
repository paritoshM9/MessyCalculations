def calcF(a,b):
    ret= a+ (b**2)
    return ret
def F(n,arr):
    
    top=len(arr)-1
    if(top==n):
        print(arr[n])
        return
    else:
        
        arr.append(calcF(arr[top],arr[top-1]))
        F(n,arr)
    
t,p,q=input().strip().split(' ')
t=int(t)
p=int(p)
q=int(q)



for i in range(t):
    arr=[]
    arr.append(0) #to make it 1-indexed
    arr.append(p)
    arr.append(q)
    n=input().strip()
    n=int(n)
    F(n,arr)
    
