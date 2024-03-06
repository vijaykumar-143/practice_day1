a=input()
sum=0
n=len(a)
for i in a:
    sum+=int(i)** n
if str(sum) == a:
    print("amstrong")
else:
    print("not amstrong")
        
#or
n,m=map(int,input().split())
for i in range(n,m+1):
    a=str(i)
    sum=0
n=len(a)
for i in a:
    sum+=int(i)** n
if str(sum) == a:
    print("amstrong")
else:
    print("not amstrong")
    
