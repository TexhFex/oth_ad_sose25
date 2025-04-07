import time
import random

def n3(matrix):
    lenght = len(matrix)
    max_sum = float("-inf")
    for top in range(lenght):
        col_sum = [0]*lenght
        for bottom in range(top, lenght):
            for col in range(lenght):
                col_sum[col] += matrix[bottom][col]

            current_sum = 0
            for val in col_sum:
                current_sum = max(val, current_sum + val)
                max_sum = max(max_sum, current_sum)
    return max_sum

def genMatrix(n, low=-10, high=10):
    return [[random.randint(low, high) for _ in range(n)] for _ in range(n)]

if __name__ == "__main__":
    candidates = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]

    for n in candidates:
        matrix = genMatrix(n)
        start_time = time.time()
        print(f"Ergebnis: {n3(matrix)}")
        elapsed = time.time() - start_time
        print(f"Für n={n}: Benötigte Time ~{elapsed} secs")

# Für n=50: Benötigte Time ~0.02 secs
# Für n=100: Benötigte Time ~0.13 secs
# Für n=150: Benötigte Time ~0.40 secs
# Für n=200: Benötigte Time ~1.05 secs
# Für n=250: Benötigte Time ~2.10 secs
# Für n=300: Benötigte Time ~3.34 secs
# Für n=350: Benötigte Time ~5.24 secs
# Für n=400: Benötigte Time ~7.98 secs
# Für n=450: Benötigte Time ~10.83 secs
# Für n=500: Benötigte Time ~14.63 secs
# Für n=600: Benötigte Time ~27.38 secs
# Für n=700: Benötigte Time ~43.77 secs
# Für n=800: Benötigte Time ~63.21 secs
# Für n=900: Benötigte Time ~89.54 secs
# Für n=1000: Benötigte Time ~128.51 secs