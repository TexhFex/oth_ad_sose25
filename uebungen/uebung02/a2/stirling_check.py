# Sterling test von ChatGPT um die differenz von log(n!) = Θ(n log n) zu sehen
# AMD Ryzen 7 7730U 8cores 16 threads 40GB Ram python3
# time for one run with n = 200000 ~ 50 seconds

import math
from multiprocessing import Pool, cpu_count

def compute_values(n):
    log_fact = math.log(math.factorial(n))
    n_log_n = n * math.log(n)
    diff = abs(log_fact - n_log_n)
    return (n, log_fact, n_log_n, diff)

def main():
    N_MAX = 200000
    STEP = 100  # Sonst sind’s zu viele Zeilen
    inputs = list(range(1, N_MAX + 1, STEP))

    print(f"Benutze {cpu_count()} Kerne…")
    print(f"{'n':>7} | {'log(n!)':>20} | {'n * log(n)':>20} | {'Differenz':>20}")
    print("-" * 75)

    with Pool() as pool:
        results = pool.map(compute_values, inputs)

    for n, log_fact, n_log_n, diff in results:
        print(f"{n:7} | {log_fact:20.5f} | {n_log_n:20.5f} | {diff:20.5f}")

if __name__ == "__main__":
    main()
