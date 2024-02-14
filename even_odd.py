n=int(input())
sum=0
j=0
if(n%2==0):
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        print("it is even and perfect number")
    else:
        print("it is even and not perfect number")
else:
    for i in range(2,n):
        if(n%i ==0):
            j=j+1
    if(j>1):
        print("it is odd and not prime")
    else:
        print("it is odd and prime")
