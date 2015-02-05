"""
PyBrain is a very simple set of calculation
exercises to wake up the brain
"""

from random import randint
import sys

def do_plus(a, b):
    val = a + b
    problem = "{0} + {1} = ".format(a, b)
    print problem,
    answer = input("")
    if answer == val:
        print "Good"
        got_it = True
    else:
        print "Wrong, it is {0}".format(val)
        got_it = False
    return [(a, b), got_it]

def do_minus(a, b):
    if a < b:
        a, b = b, a
    val = a - b
    problem = "{0} - {1} = ".format(a, b)
    print problem,
    answer = input("")
    if answer == val:
        print "Good"
        got_it = True
    else:
        print "Wrong, it is {0}".format(val)
        got_it = False
    return [(a, b), got_it]

def do_multiplication(a, b):
    val = a * b
    problem = "{0} x {1} = ".format(a, b)
    print problem,
    answer = input("")
    if answer == val:
        print "Good"
        got_it = True
    else:
        print "Wrong, it is {0}".format(val)
        got_it = False
    return [(a, b), got_it]

def do_division(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        b = 1
    if a == 0:
        a = 1
    val = a / b
    ret_val = a % b
    problem = "{0} / {1} = ".format(a, b)
    print problem,
    answer = input("")
    if ret_val:
        print "and return",
        ret_ans = input("")
        ret_p = " {0}".format(ret_val)
    else:
        ret_ans = 0
        ret_p = ""
    if answer == val and ret_ans == ret_val:
        print "Good"
        got_it = True
    else:
        print "Wrong, it is {0}{1}".format(val, ret_p)
        got_it = False
    return [(a, b), got_it]

dispatch = {
        0:do_plus,
        1:do_minus,
        2:do_multiplication,
        3:do_division,
        }

def math_brain(rounds, max_num):
    # round
    results = []
    for i in range(rounds):
        # choose values
        a = randint(0, max_num)
        b = randint(0, max_num)
        # choose +, -, * or /
        prob_list = dispatch[randint(0, 3)](a, b) 


    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        r = sys.argv[1]
    else:
        r = 50
    if len(sys.argv) > 2:
        m = sys.argv[2]
    else:
        m = 14
    math_brain(r, m)
    print "Done"
    
