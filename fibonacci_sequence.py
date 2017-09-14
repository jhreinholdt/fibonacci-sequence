# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:29:37 2017

@author: jhreinholdt

Problem: Fibonacci Sequence 
- Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.
Caution: Will run slow for sequences over 30 elements.
"""

def fibonacci_number(numberNth):
    if numberNth == 0:
        return 0
    elif numberNth == 1:
        return 1
    else:
        return (fibonacci_number(numberNth - 2) + fibonacci_number(numberNth - 1))

def fibonacci_sequence(number):
    if number <= 0:
        return print("Please enter a positive integer")
    else: 
        print("The Fibonacci Sequence with", number, "elements is:") 
        for k in range(number):
            print(fibonacci_number(k),"",end="")

def main():
    while True:
        fibonacci_sequence(int(input('\nEnter a positive number to generate the Fibonacci Sequence with that amount of elements: ')))
        
if __name__ == '__main__':
    main()
