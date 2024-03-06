"""write a pythom program to print the odd
numbers in desending order without duplicates"""

l=list(map(int,input().split()))
lst=[]
for i in l:
    if ((i not in lst) and (i%2!=0)):
        lst.append(i)
for i in range(0,len(lst)):
    a=max(lst)
    print(a)
    lst.remove(a)
