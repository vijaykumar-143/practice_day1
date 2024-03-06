#program to print smallest vowel which is repeating in odd times
"""
n=input()
s=""
s=['a','e','i','o','u']
n.lower()
c=1
for i in n:
    if i in s:
        count1=n.count(i)
        if(count1>0 and (count1%2)!=0):
            num=count1
            ch=i
    
print(ch ,"  :",count1)

#or
"""
s=input()
s1=""
for i in s:
    if i in "aeiouAEIOU":
        if s.count(i)%2!=0:
            s1+=i
print(min(s1))
        
