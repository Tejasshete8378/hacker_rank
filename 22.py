#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    capitalized_words = [word.capitalize() if word else word for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':

    s = input()

    result = solve(s)

    
