import numpy as np
import time

# --------------------------------------------------
# 1. ARRAY CREATION, INDEXING, SLICING
# --------------------------------------------------

# Create an array
arr = np.arange(1, 21).reshape(4, 5)
print("Array:\n", arr)

# Indexing
print("\nElement at (1,2):", arr[1, 2])

# Slicing
print("\nFirst two rows:\n", arr[:2])
print("\nLast column:\n", arr[:, -1])

# --------------------------------------------------
# 2. MATHEMATICAL + AXIS-WISE + STATISTICAL OPERATIONS
# --------------------------------------------------

print("\nElement-wise square:\n", arr ** 2)
print("\nRow-wise sum:", arr.sum(axis=1))
print("Column-wise mean:", arr.mean(axis=0))
print("Overall standard deviation:", arr.std())

# --------------------------------------------------
# 3. RESHAPING & BROADCASTING
# --------------------------------------------------

reshaped = arr.reshape(10, 2)
print("\nReshaped (10x2):\n", reshaped)

# Broadcasting example: subtract column means
col_means = arr.mean(axis=0)
normalized = arr - col_means
print("\nBroadcasted (normalized):\n", normalized)

# --------------------------------------------------
# 4. SAVE / LOAD NUMPY ARRAY
# --------------------------------------------------

np.save("my_array.npy", arr)
loaded_arr = np.load("my_array.npy")
print("\nLoaded array:\n", loaded_arr)

# --------------------------------------------------
# 5. PERFORMANCE COMPARISON: NUMPY VS PYTHON LIST
# --------------------------------------------------

# Python list
list_data = list(range(1_000_000))

start = time.time()
list_sum = sum(list_data)
end = time.time()
print("\nPython list sum time:", end - start, "seconds")

# NumPy array
np_data = np.arange(1_000_000)

start = time.time()
np_sum = np_data.sum()
end = time.time()
print("NumPy sum time:", end - start, "seconds")
