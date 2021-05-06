def minion_game(s):
    # your code goes here
    V=['A','E','I','O','U']
    Kevin=0
    Stuart=0
    l=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
    for k in l:
        if(k[0] in V):
            Kevin=Kevin+1
        else:
            Stuart=Stuart+1
    if(Stuart>Kevin):
        print("Stuart",Stuart)
    else:
        print("Kevin",Kevin)
    return()
s=str(input())
minion_game(s)
