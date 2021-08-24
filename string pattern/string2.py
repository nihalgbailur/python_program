# 1
# 12
# 123
# 1234
# 12345

num = int(input("enter the number"))
for r in range(1,num+1):
    for c in range(1,r+1):
        print(c,end=" ")
    print()