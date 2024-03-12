def fizzbuzz(n):
    divisivel_3 = False
    divisivel_5 = False
    if(n % 3 == 0):
        divisivel_3 = True
    if(n % 5 == 0):
        divisivel_5 = True
    if(divisivel_3 == True) and (divisivel_5 == False):
        return "Fizz"
    elif(divisivel_3 == False) and (divisivel_5 == True):
        return "Buzz"
    elif(divisivel_3 == True) and (divisivel_5 == True):
        return "FizzBuzz"
    else:
        return n

