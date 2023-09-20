def hanno(n,a,b,c):
    if n>0:
        hanno(n-1,a,c,b)
        print("从%s移动到%s" % (a,c))
        hanno(n-1,b,c,a)
hanno(3,'A','B','C')
