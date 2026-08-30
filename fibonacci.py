def fibonacci(n):
    """Retourne une liste des n premiers nombres de Fibonacci."""
    suite = []
    a, b = 0, 1
    for _ in range(n):
        suite.append(a)
        a, b = b, a + b
    return suite


if __name__ == "__main__":
    for nombre in fibonacci(10):
        print(nombre)
