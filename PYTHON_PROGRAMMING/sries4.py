n=int(input("enter rows"))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j%2,end=" ")
    print("\n")
