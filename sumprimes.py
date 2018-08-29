def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i==0:
            flist=flist+[i]     
    
    if len(flist) == 2:
        return(n)
    else:
        return 0
    
        

def sumprimes(l):
    sum = 0
    for i in range (0,len(l)):
        if factors(l[i])!=0:
            sum = sum + l[i]
    return(sum)
    