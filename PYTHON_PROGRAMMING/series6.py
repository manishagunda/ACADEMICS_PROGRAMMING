n=int(input("enter rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+j),end=" ")
    print("\n")
