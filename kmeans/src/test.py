import numpy as np
import random

arr = np.array([1, 234, 12, 34, 23, 412, 412, 412, 3, 1, 2, 412, 32, 1])

labels = [random.choice([True, False]) for i in range(len(arr))]
print(arr)
print(labels)

print(arr[labels])