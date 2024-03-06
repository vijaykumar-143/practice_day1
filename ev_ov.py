n=input()
ev=0
ov=0
r=len(n)
s=['a','e','i','o','u','A','E','I','O','U']
for i in range(r):
    if(i%2)==0:
        if n[i] in s:
            ev+=1
    else:
        if n[i] in s:
            ov+=1
print("odd vowels:" ,ov)
print("even vowels:",ev)

#or

"""
s=input()
s1=s[::2]
s2=s[1::2]
ev=s1.count("a")+s1.count("e")+s1.count("i")+s1.count("o")+s1.count("u")
ov=s2.count("a")+s2.count("e")+s2.count("i")+s2.count("o")+s2.count("u")
print("even count",ev,"\nodd count",ov)   


""" 
    
     
    
