def lcm(a,b):
    i = 1
    if(a>b):
        a,b=b,a
    while(b%a!=0):
        b*=i
        i+=1
    return b
a,b = map(int,input().split())
print(lcm(a,b))
