# -*- coding: utf-8 -*-


def fizzbuzz(number):
    if str(number).count('3') > 0 or number % 3 ==0:
        if number % 7 > 0 and number % 15 > 0:
            return 'Fizz'
    elif number % 5 == 0 and number % 15 > 0 and number % 7 > 0:
        return 'Buzz'

    elif number % 7 == 0 and number % 3 > 0 and number % 5 >1:
        return 'Woof'
    elif number % 15 == 0:
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

def contains3char(number):
    return str(number).count('3') > 0

def say_hello(name):
    return "Hello "+name

def main():
    numbers = range(1,101)

    for number in numbers:
        print str(number) +" : "+ str(fizzbuzz(number))
main()
