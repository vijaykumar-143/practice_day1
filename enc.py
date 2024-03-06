n=input("")
k=int(input())
m=""
for i in n:
    x=ord(i)+k
    if(x>=123):
        x=x-122
        x=96+x
    m=m+chr(x)
print(m)
    
    

      

