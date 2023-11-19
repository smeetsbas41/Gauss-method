import numpy as np

# functhion  for solve
def gauss_elimination(A, b):
    n = len(A)
    # go line
    for i in range(n-1):
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # another
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# example of line 
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

# solving
solution = gauss_elimination(A, b)
print("solution:", solution)
