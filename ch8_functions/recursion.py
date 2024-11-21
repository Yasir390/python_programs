
# recursion

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n =int(input('enter a number : '))
print(f'The factorial of this num is : {factorial(n)}')

#great explained code with harry timestamp 5:15:10