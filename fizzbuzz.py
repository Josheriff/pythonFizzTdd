# -*- coding: utf-8 -*-


def fizzbuzz(number):
    if str(number).count('3') > 0:
        return 'Fizz'
    elif number % 7 == 0:
        return 'Woof'
    elif number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number

def say_hello(name):
    return "Hello "+name

def main():
    numbers = range(1,101)

    for number in numbers:
        print str(number) +" : "+ str(fizzbuzz(number))
main()
