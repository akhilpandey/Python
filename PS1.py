import random
import sys
import os
import math

## http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/assignments/

# Prime Numbers problem
primeNumbers = [2]

def getNthPrimeNumeber(n):

    ## check if we have enough prime numbers already
    if (n > len(primeNumbers)):

        ## start from theNumber 3
        theNumber = 3

        while (n > len(primeNumbers)):

            ## check if the number is prime
            if (isPrime(theNumber)):
                primeNumbers.append(theNumber);

            ## increment theNumber
            theNumber += 1;

     ## return the nth prime number
    return primeNumbers[n - 1]


def isPrime(x):
    for preX in primeNumbers:

        if x % preX == 0:

            return False

    return True




## Problem 2
def getLogSumOfNumUptoNthPrimeNumeber(n):
    the_sum = 0;

    ## create the list of prime numbers upto the number n
    getNthPrimeNumeber(n);

    for a_num in primeNumbers:
        the_sum += math.log(a_num);


    print(the_sum, n, the_sum/n);

getLogSumOfNumUptoNthPrimeNumeber(5);



