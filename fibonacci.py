import argparse


def fibonacci(n):
    """Retourne une liste des n premiers nombres de Fibonacci."""
    suite = []
    a, b = 0, 1
    for _ in range(n):
        suite.append(a)
        a, b = b, a + b
    return suite


if __name__ == "__main__":
    parseur = argparse.ArgumentParser(
        description="Affiche les n premiers nombres de la suite de Fibonacci."
    )
    parseur.add_argument(
        "combien",
        nargs="?",
        type=int,
        default=10,
        help="nombre de termes a afficher (10 par defaut)",
    )
    args = parseur.parse_args()

    if args.combien < 0:
        parseur.error("le nombre de termes doit etre positif ou nul")

    for nombre in fibonacci(args.combien):
        print(nombre)
