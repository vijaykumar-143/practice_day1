a,b,c,g,h,s=map(int,input().split())
r=input()
cc=input()
l=input()
f=input()
d=input()
ss=input()
if(a<=6):
    print("go to study & get ready");
    if(r =="yes"):
        print("pack box and go to busstop");
        if(b>=8):
            print("sit in bus")
            if(c<=9):
                print("enter to college")
                if(cc=="yes"):
                    print("listen to classes")
                    if(l=="yes"):
                        print("have lunch and listen next classes")
                        if(g<=5):
                            print("go and sit in the bus")
                            if(h<=6):
                                print("go to home")
                                if(f=="yes"):
                                    print("have dinner")
                                    if(d=="yes"):
                                        print("go to study")
                                        if(s>=2):
                                            print("go to sleep")
                                            if(ss=="yes"):
                                                print("go to sleep & good night")
                                            else:
                                                print("don't sleep")
                                        else:
                                            print("complete 2 hours study")
                                    else:
                                        print("have your dinner first")
                                else:
                                    print("first go and freshup")
                            else:
                                print("go to home quickly")
                        else:
                            print("go to busstop fastly")
                    else:
                        print("first have your lunch")
                else:
                    print("go to class in time")
            else:
                print("go to college in time")
        else:
            print("go to busstop before 8")
    else:
        print("get ready in time")
else: 
    print("wakeup before 6 am")
