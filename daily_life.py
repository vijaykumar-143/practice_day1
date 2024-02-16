a,b,c,g,h,s=map(int,input().split())
r=input()
cc=input()
l=input()
f=input()
d=input()
ss=input()
if(a<=6):
    print("good moring have a nice day it's 6'o' clock, go to study & get ready");
    if(r =="yes"):
        print("pack box and go to busstop before 8 AM");
        if(b>=8):
            print("select your seat and sit in bus ")
            if(c<=9):
                print("enter to college &go to class before 9:05AM")
                if(cc=="yes"):
                    print("listen to classes attentively from 9AM to 12:40PM")
                    if(l=="yes"):
                        print("have lunch before 1:30PM and listen to classes upto 5PM")
                        if(g<=5):
                            print(" you reached college bus stand before 5:10 take your seat in the bus")
                            if(h<=6):
                                print("go to home and have your works")
                                if(f=="yes"):
                                    print("first get freshup before 7:30 PM and have your  dinner ")
                                    if(d=="yes"):
                                        print("after having your dinner study for 2 hours from 8 PM to 10PM")
                                        if(s>=2):
                                            print("go to sleep after study")
                                            if(ss=="yes"):
                                                print("it's 10P< go to sleep & good night")
                                            else:
                                                print("don't sleep your work is not completed")
                                        else:
                                            print("complete 2 hours study")
                                    else:
                                        print("have your dinner first before 7:30/8PM")
                                else:
                                    print("first go and freshup ")
                            else:
                                print("go to home before 6:20PM to complete your works")
                        else:
                            print("reach college bus stand before 5:10 to get a seat in the bus")
                    else:
                        print("first have your lunch in time to attend classes")
                else:
                    print("go to class in time to get attendence")
            else:
                print("go to college in time ,it's late come to college tommarow")
        else:
            print("go to busstop before 8,bus already left")
    else:
        print("get ready in time ,it's time to go to bus stop")
else: 
    print("wakeup it's 6AM ,this is not good to sleep after 6 AM")
