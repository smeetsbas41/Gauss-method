import numpy as np

# Функция для решения системы линейных уравнений методом Гаусса
def gauss_elimination(A, b):
    n = len(A)
    # Прямой ход
    for i in range(n-1):
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Обратный ход
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# Пример системы линейных уравнений
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])
b = np.array([8, -11, -3])

# Решаем систему уравнений
solution = gauss_elimination(A, b)
print("Решение системы уравнений:", solution)
