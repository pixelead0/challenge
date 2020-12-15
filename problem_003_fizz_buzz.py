#!/bin/python3

"""
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz"
  instead of the number.
"""
for i in range(1, 101):
    print("Fizz" * (i % 3 < 1) + (i % 5 < 1) * "Buzz" or i)
