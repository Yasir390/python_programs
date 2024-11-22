
def patternUsingRecursion(n):
    if(n == 0):
        return 
    print('*'*n)
    patternUsingRecursion(n-1)

patternUsingRecursion(5)


"""

*****
****
*** 
**  
* 

"""