# -*- coding: utf-8 -*-

from expects import *
from fizzbuzz import *

with describe('Fizzbuzz'):
  #  with context('when saying hello to Foo'):
  #      with it('says Hello to Foo'):
  #          name = 'Foo'
#
#            result = say_hello(name)
#
#            expect(result).to(equal('Hello Foo'))
 #   with context('When number is one'):
#        with it('return 1'):
#            number = 1
#
#            result = fizzbuzz(number)
#
#            expect(result).to(equal(1))

   # with context ('When number is 3'):
#        with it('Returns Fizz'):
#            number = 3
#
#            result = fizzbuzz(number)
#
#            expect(result).to(equal('Fizz'))

   # with context ('When number is 5'):
#        with it('Returns Buzz'):
#            number = 5
#
#            result = fizzbuzz(number)
#
#            expect(result).to(equal('Buzz'))
#    with context ('When number is 15'):
#        with it('Returns FizzBuzz'):
#            number = 15
#
#            result = fizzbuzz(number)

#            expect(result).to(equal('FizzBuzz'))

    with context ('When number is divisible by 3 and not by 5'):
        with it('Returns Fizz'):
            numbers = [6, 9, 12]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal('Fizz'))

    with context ('When number is divisible by 5 and not by 3'):
        with it('Returns Fizz'):
            numbers = [5, 10, 20, 100]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal('Buzz'))

    with context ('When number is divisible by 15 and does not have a 3'):
        with it('Returns FizzBuzz'):
            numbers = [15, 45, 60, 75, 90]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal('FizzBuzz'))
    with context ('When is not divisible for 3 or 5 or 7'):
        with it('Returns the number'):
            numbers = [1,2,4]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal(number))

    with context ('When number is divisible by 7 and donest hava a 3'):
        with it('Returns Woof'):
            numbers = [7, 14, 21, 28, 42, 49, 56, 70, 77, 84, 91, 98]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal('Woof'))
    with context ('When number contains a 3'):
        with it('Returns Fizz'):
            numbers = [3,13,23,30,33,43,53,63,73,83,93]

            for number in numbers:
                result = fizzbuzz(number)

                expect(result).to(equal('Fizz'))

