# Python Program to Find the Second Largest Number in a List?


def secondlargest(list1):
    list1.sort()
    return list1[-2]


list1 = [1,34,2,12233,43443,2]
print(secondlargest(list1))



# Python Program to Find the Second Largest Number in a List without using the sort() Function?


def secondlargest(list1):
    largest = list1[0]
    secondlargest = list1[0]
    for i in list1:
        if i > largest:
            secondlargest = largest
            largest = i
        elif i > secondlargest and i < largest:
            secondlargest = i
    return secondlargest


list1 = [1,34,2,12233,43443,2]
print(secondlargest(list1))






