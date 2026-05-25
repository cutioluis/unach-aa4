import time
import math
import numpy as np

# ── Técnica 1: raíz cuadrada + list comprehension 
def es_primo_opt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))

def encontrar_primos_opt(limite):
    return [n for n in range(2, limite + 1) if es_primo_opt(n)]

# ── Técnica 2: Criba de Eratóstenes con NumPy 
def criba_numpy(limite):
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[0:2] = False
    for i in range(2, int(np.sqrt(limite)) + 1):
        if es_primo[i]:
            es_primo[i*i::i] = False
    return np.nonzero(es_primo)[0]

if __name__ == "__main__":
    # Versión list comprehension + sqrt
    t0 = time.time()
    primos_lc = encontrar_primos_opt(100_000)
    t1 = time.time()
    print(f"[LC + sqrt]  Primos: {len(primos_lc)}  |  Tiempo: {t1 - t0:.4f} s")

    # Versión NumPy (criba)
    t2 = time.time()
    primos_np = criba_numpy(100_000)
    t3 = time.time()
    print(f"[NumPy]      Primos: {len(primos_np)}  |  Tiempo: {t3 - t2:.4f} s")