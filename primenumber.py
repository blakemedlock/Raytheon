def isPrime(num): 
    if num < 2:
        return 0 
        #0 and 1 are not prime
    else:
        x = num // 2
        #only will check half of the numbers up to it
        for j in range(2, x + 1):
            if num % j == 0: 
            #if the result is 0 after using the modular function it isn't prime
                return 0
                #returns false if it is not prime
    return 1
    #returns true if it has no factors



for i in range(1, 100):
#loops for all numbers 1 to 100
    if isPrime(i):
    #if the isprime function returns true the number is printed
        print(i, end=" ")
