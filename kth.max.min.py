""" write a program to find kth largest and kth smallest number"""
lst=list(map(int,input().split()))
lst.sort()
print("enter k th element: ")
k=int(input())
print(f"{k}minimum is {lst[k-1]}")
print(f"{k}maximum is {lst[-k]}")
