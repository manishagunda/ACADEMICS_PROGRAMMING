n=int(input("enter num"))
t=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(t==r):
    print("palindrome")
else:
    print("not palindrome")