# p
# yy
# ttt
# hhhh
# ooooo
# nnnnnn string python in right triangle state
# hint : nested for loop

str1 = input("enter the string name: ")
for r in range(len(str1)):
    for c in range(r+1):
        print(str1[r],end="")
    print()
    
