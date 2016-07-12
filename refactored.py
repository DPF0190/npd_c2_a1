

'''for the integers 1 through 50 find the sum of even numbers MINUS the sum of numbers that are divisible by 7'''

#define even integers 1-50
#define numbers divisible by 7
#sum two parts
#subtract numbers div by 7 from sum of even integers

import math

def get_even():
    return list(range(0, 50, 2))

def get_sevs():
    return list(range(0, 50, 7))

def solve_problem():
    numa = get_even()
    numsum = (sum(numa))
    numb = get_sevs()
    numsumb = (sum(numb))
    return numsum - numsumb

if __name__ == '__main__':
       print(solve_problem())

