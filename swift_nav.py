# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:23:28 2017

@author: A
"""
def fib(n): #generate fibbonacci numbers through recursion
    if n < 2: 
        return n 
    else: 
        return fib(n-1) + fib(n-2)
        
def primeChecker(n): #checking for prime numbers
    if n < 2: 
        return False
    if n == 2: 
        return True
    if not n & 1: 
        return False
    if n > 2: 
        for i in range(3,int(n**0.5)+1,2):#need to go up to the square root of n + 1, the range accounts for it by starting from 3, this part was taken from a forum on stack overflow
            if n%i == 0:
                return False
            
    return True
def divisibleChecker(n):
    a = primeChecker(n)
    if a == False:
       if n % 15 ==0: 
            print("Buzz, Fizz, FizzBuzz")
       elif (not(n % 3 ==0) and not(n%5 ==0) and not(n % 15 ==0)): #Check for all three because it was giving me bugs and printing corresponding fibbonacci numbers regardless
            print("corresponding fibbonacci number:", n)
       elif n % 3 == 0: 
                print("Buzz")
       elif n % 5 == 0:
                 print("Fizz")
    elif a == True: 
       
        if n == 3: 
            print("Buzz, BuzzFizz")
        elif n == 5: 
            print("Fizz, BuzzFizz")
        else: 
             print("BuzzFizz")
    
results = []          
n = int(input("Please enter a number:"))
for i in range(1,n):
    #print(fib(i))
    results.append(divisibleChecker(fib(i)))
   # print(fib(i))
    
