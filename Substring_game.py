def substring(s):
    V=['A','E','I','O','U']
    Kevin=0
    Stuart=0
    l=[]
    rp={}
    a=len(s)
    for i in range(a):
        p=s[i:a]
        for j in range(len(p)):
            w=p[0:len(p)-j]
            count=1
            if(w in l):
                count=count+1
                rp[w]=rp[w]+1
            else:
                rp[w]=count
            l.append(w)
    print(rp)
    for k in rp:
        if(k[0] in V):
            Kevin=Kevin+rp[k]
        else:
            Stuart=Stuart+rp[k]
    return(max([Kevin,Stuart]))
s=input("Enter:")
print(substring(s))
