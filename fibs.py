import time


def fib(number):
    if number == 0:
      return 0
    elif number == 1:
      return 1
    else:
      return fib(number-1) + fib(number-2)

#starts counting at 0
print "What number to fibonacci?"
number = raw_input()
number = int(number)
start= time.clock()
print (str(fib(number)))
end = time.clock()
total= str(end-start)
print ("it took " + total + " seconds to do this.")
