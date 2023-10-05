#!/usr/bin/env python3
'''Lab 3 Part 1 script - Functions'''
# Author ID: ddelgado

def sum_numbers(number1, number2):
    sum = number1 + number2
    return sum

def subtract_numbers(number1, number2):
    subtract_sum = number1 - number2
    return subtract_sum

def multiply_numbers(number1, number2):
    multiply_sum = number1 * number2
    return multiply_sum

if __name__ == '__main__':
    print(sum_numbers(10,5))
    print(subtract_numbers(10,5))
    print(multiply_numbers(10,5))
