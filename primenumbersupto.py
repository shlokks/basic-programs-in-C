def factors(n):
    flist=[]
    for i in range[1:n+1]:
        if n%i==0:
            print(i)
            flist=flist+[i]
            return(flist)              
    
def isprime(n):
    return(factors(n)==[1,n])

def primesupto(n):
    primelist=[]
    for i in range[1:n+1]:
        if isprime(i):
            primelist=primelist+[i]
            return(primelist)
            
            
    