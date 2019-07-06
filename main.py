#  __    __  ____    __    ____       _____  
# |  |  |  | \   \  /  \  /   /      | ____| 
# |  |__|  |  \   \/    \/   / ______| |__   
# |   __   |   \            / |______|___ \  
# |  |  |  |    \    /\    /          ___) | 
# |__|  |__|     \__/  \__/          |____/  
#                                            

# Check if a number is prime
def isPrime(n): 
  # Corner case 
  if n <= 1: 
    return False

  # Check from 2 to n-1 
  for i in range(2, n): 
    if n % i == 0: 
      return False; 
  return True

# FizzBuzz Program!
#  multiples of three print "Fizz" instead of the number and 
#  for the multiples of five print "Buzz". If debug argument is true, prints the number beteewn square brackets.
def fizzBuzz(limit, debug=0):
  for n in range(1, limit+1):
    d = ""
    if debug:
      d= "[" + str(n) + "]"
    if n % 3 == 0 and n % 5 == 0:
      print("FizzBuzz", d)
    elif n % 3 == 0:
      print("Fizz", d)
    elif n % 5 == 0:
      print("Buzz", d)
    elif isPrime(n):
      print("Prime", d)
    else:
        print(n)

# test this fizzBuzz function up to 100
# fizzBuzz(100)

# Now we will use the debug flag to see all numbers
fizzBuzz(100, 1)