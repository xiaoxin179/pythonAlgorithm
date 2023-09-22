def hanno(n,a,b,c):
    if n>0:
        hanno(n-1,a,c,b)
        print("从%s移动到%s" % (a,c))
        hanno(n-1,b,a,c)
hanno(4,'A','B','C')
