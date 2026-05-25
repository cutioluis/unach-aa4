import time


def es_primo(n):
    if n < 2:
        return False

    # Itera hasta n (ineficiente)
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def encontrar_primos(limite):
    primos = []

    for num in range(2, limite + 1):
        if es_primo(num):
            primos.append(num)

    return primos


if __name__ == "__main__":
    inicio = time.time()

    primos = encontrar_primos(100_000)

    fin = time.time()

    print(f"Números primos encontrados: {len(primos)}")
    print(f"Tiempo de ejecución (original): {fin - inicio:.4f} segundos")