# test_lib.py

import time


def timer(func, args):
    """Returns 1) the time taken to execute a function with given arguments, and 2) the return value of the function. For multiple iterations, call timer() repeatedly and sum the results.
    
    timer(f: function(a -> b), args: list) -> (float, b)
    """
    start = time.time()
    val = func(*args)
    end = time.time()
    return (end - start, val)