import random, time, sys

def rand_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split(M):
    n = len(M) // 2
    return (
        [row[:n] for row in M[:n]],   # 11
        [row[n:] for row in M[:n]],   # 12
        [row[:n] for row in M[n:]],   # 21
        [row[n:] for row in M[n:]]    # 22
    )

def join(C11, C12, C21, C22):
    n2 = len(C11)
    n  = n2 * 2
    C = [[0.0]*n for _ in range(n)]
    for i in range(n2):
        C[i][:n2]     = C11[i]
        C[i][n2:]     = C12[i]
        C[i+n2][:n2]  = C21[i]
        C[i+n2][n2:]  = C22[i]
    return C

def standard(A, B):
    n = len(A)
    C = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            aik = A[i][k]
            for j in range(n):
                C[i][j] += aik * B[k][j]
    return C

def var2(A, B, cutoff=64):
    n = len(A)
    if n <= cutoff or n % 2:
        return standard(A, B)

    M11, M12, M21, M22 = split(A)
    N11, N12, N21, N22 = split(B)

    H1 = var2(add(M11, M22), add(N11, N22), cutoff)
    H2 = var2(add(M21, M22), N11, cutoff)
    H3 = var2(M11, sub(N12, N22), cutoff)
    H4 = var2(M22, sub(N21, N11), cutoff)
    H5 = var2(add(M11, M12), N22, cutoff)
    H6 = var2(sub(M21, M11), add(N11, N12), cutoff)
    H7 = var2(sub(M12, M22), add(N21, N22), cutoff)

    C11 = add(sub(add(H1, H4), H5), H7)
    C12 = add(H3, H5)
    C21 = add(H2, H4)
    C22 = add(sub(add(H1, H3), H2), H6)

    return join(C11, C12, C21, C22)

if __name__ == "__main__":
    n = 256
    A = rand_matrix(n)
    B = rand_matrix(n)

    t0 = time.time()
    C_std = standard(A, B)
    t1 = time.time() - t0

    t0 = time.time()
    C_str = var2(A, B, cutoff=64)
    t2 = time.time() - t0
    print(f"Normal : \t{t1}s")
    print(f"var2 : \t\t{t2}")
