import argparse


def statistiques(nombres):
    """Retourne un dictionnaire de statistiques de base pour une liste de nombres."""
    effectif = len(nombres)
    return {
        "nombre": effectif,
        "somme": sum(nombres),
        "moyenne": sum(nombres) / effectif,
        "minimum": min(nombres),
        "maximum": max(nombres),
    }


if __name__ == "__main__":
    parseur = argparse.ArgumentParser(
        description="Affiche des statistiques de base pour une liste de nombres."
    )
    parseur.add_argument(
        "nombres",
        nargs="+",
        type=float,
        help="les nombres a analyser (au moins un)",
    )
    args = parseur.parse_args()

    resultats = statistiques(args.nombres)
    for nom, valeur in resultats.items():
        print(f"{nom} : {valeur}")
