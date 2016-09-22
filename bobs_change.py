"""
Problem:

    Bob would like to buy some sweets, which cost 50p.
    Bob has some money but, unfortunately, Bob is only 3
    and has no concept of money yet. Bob's solution to this
    is to just hand over the whole of his change and hope the
    shopkeeper will sort it out for him.

    The function bobs_change takes in a number representing
    how much money Bob has handed over (in pence). It should print
    the amount of change owed if he has enough, or
    "Sorry Bob, you don't have enough" if he is short.

Tests:

    >>> bobs_change(80)
    30
    >>> bobs_change(132)
    82
    >>> bobs_change(50)
    0
    >>> bobs_change(40)
    Sorry Bob, you don't have enough
   
"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code:
def bobs_change(money):

    if money < 50:
        print ("Sorry Bob, you don't have enough")


    if money >=50:
        print (money-50)


