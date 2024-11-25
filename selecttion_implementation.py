import random
import time
import numpy as np
import pandas as pd

# Deterministic algorithm for selecting the k-th smallest element (Median of Medians)
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide array into chunks of 5 and sort them
    chunks = [sorted(arr[i:i + 5]) for i in range(0, len(arr), 5)]
    medians = [chunk[len(chunk) // 2] for chunk in chunks]

    # Recursively find the median of medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partition around the pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# Randomized Quickselect algorithm
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return randomized_quickselect(highs, k - len(lows) - len(pivots))

# Performance analysis
def performance_analysis(input_sizes, num_trials):
    results = []
    for n in input_sizes:
        for trial in range(num_trials):
            arr = random.sample(range(1, n * 10), n)  # Unique elements
            k = random.randint(0, n - 1)
            
            # Deterministic
            start_time = time.time()
            deterministic_result = median_of_medians(arr, k)
            deterministic_time = time.time() - start_time
            
            # Randomized
            start_time = time.time()
            randomized_result = randomized_quickselect(arr, k)
            randomized_time = time.time() - start_time
            
            # Verify correctness
            correct = sorted(arr)[k] == deterministic_result == randomized_result
            results.append({
                "Input Size": n,
                "Trial": trial + 1,
                "Deterministic Time": deterministic_time,
                "Randomized Time": randomized_time,
                "Correct": correct
            })
    return pd.DataFrame(results)

# Define input sizes and number of trials
input_sizes = [10, 100, 1000, 5000, 10000]
num_trials = 5

# Perform the analysis
results_df = performance_analysis(input_sizes, num_trials)

# Display the results to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Selection Algorithm Performance Analysis", dataframe=results_df)
