# range function
# range(start, stop, step)
# start	Optional.    An integer number specifying at which position to start. Default is 0
# stop	Required.    An integer number specifying at which position to stop (not included).
# step	Optional.    An integer number specifying the incrementation. Default is 1

# When user call range() with one argument, user will get a series of numbers that starts at 0 and includes every whole number up to, but not including, the number that user have provided as the stop. 


x = range(5)
for n in x:
  print(n)



y = range(3, 20, 2)
for i in y:
  print(i)