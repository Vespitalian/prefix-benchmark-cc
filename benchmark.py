import time
import numpy as np
import pandas as pd
from english import SIXES

# The slow
prefixes = ['c','ca','car','care','cares']

def valid_prefix_slow(prefix, word_list): # My code
    for i in range(len(prefix)):
        for word in word_list:
            if word[:i+1] == prefix:
                return True
            else:
                pass
    return False


# The medium
def valid_prefix_med(prefix, word_list): # The improvement that I came up with for my code
    for word in word_list:
        if prefix == word[:len(prefix)]:
            return True
    return False

# The fast
def valid_prefix_fast(prefix, word_list): # The Calvin solution
    return any(word.startswith(prefix) for word in word_list)

results = []
def run():
    for prefix in prefixes:
        start_slow = time.time() # Getting time before we call function
        for i in range(10000): # Repeating the function 10,000 times to have a bigger number :)
            valid_prefix_slow(prefix,SIXES)
        end_slow = time.time() # End timer
        slow_time = end_slow - start_slow # The difference between start and the end time

        start_med = time.time()
        for i in range(10000):
            valid_prefix_med(prefix, SIXES)
        end_med = time.time()
        med_time = end_med - start_med

        start_fast = time.time()
        for i in range(10000):
            valid_prefix_fast(prefix, SIXES)
        end_fast = time.time()
        fast_time = end_fast - start_fast
        
        results += [[slow_time, med_time, fast_time]]

    df = pd.DataFrame(data=np.array(results))
    df.to_csv('benchmark_results.csv')

if __name__ == '__main__':
    run() # Added to import prefixes to midterm without runnning this file