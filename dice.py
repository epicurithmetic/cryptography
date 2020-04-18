# Dice simulator
import time
import random

# Reverse a string.
def reverse_string(init_string):

    init_list = list(init_string)
    rev_list = init_list[::-1]
    rev_string = ""
    for x in rev_list:
        rev_string += x

    return rev_string

#           Idea:   If we need to run a simulation to provide a selection
#                   of random numbers, then simply using the last few
#                   digits of the time may not be appropriate.
#                   The regularity in the running time of the code seems
#                   to cause uniform, rather than random, results.
#
#                   One number pulled out of no where is not random.
#                   Randomness is a property of a sequence of numbers.
