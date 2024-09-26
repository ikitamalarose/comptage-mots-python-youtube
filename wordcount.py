import sys


def word_count_dict(filename):
    """
        Lit le fichier donné, compte le nombre d'occurrences de chaque mot,
        et retourne un dictionnaire où les clés sont les mots et les valeurs sont leurs comptes.

        Args:
            filename (str): Le nom du fichier à lire.

        Returns:
            dict: Un dictionnaire avec les mots en tant que clés et le nombre d'occurrences comme valeurs.
        """
    word_count = {}
    input_file = open(filename, "r", encoding="utf-8")
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] = word_count[word] + 1
    input_file.close()
    return word_count


def print_words(filename):
    """
       Lit le fichier, compte et affiche chaque mot et son nombre d'occurrences dans l'ordre alphabétique.

       Args:
           filename (str): Le nom du fichier à lire.
       """
    word_count = word_count_dict(filename)
    for word in sorted(word_count):
        print(word, word_count[word])


def get_count(word_count_tuple):
    """
       Retourne le nombre d'occurrences à partir d'un tuple (mot, compte).
       Utilisé pour le tri des mots en fonction de leur fréquence.

       Args:
           word_count_tuple (tuple): Un tuple contenant un mot et son compte.

       Returns:
           int: Le nombre d'occurrences du mot.
       """
    return word_count_tuple[1]


def print_top(filename):
    """
       Affiche les 20 mots les plus fréquents dans le fichier, avec leur nombre d'occurrences,
       triés du plus fréquent au moins fréquent.

       Args:
           filename (str): Le nom du fichier à lire.
       """
    word_count = word_count_dict(filename)
    items = sorted(word_count.items(), key=get_count, reverse=True)
    for item in items[:20]:
        print(item[0], item[1])


def main():
    """
       Fonction principale qui analyse les arguments de la ligne de commande et appelle les fonctions
       `print_words` ou `print_top` en fonction de l'option spécifiée.
       Si les arguments sont incorrects, elle affiche un message d'usage.

       Args:
           sys.argv[1]: L'option à utiliser, soit '--count' soit '--topcount'.
           sys.argv[2]: Le nom du fichier à traiter.
       """
    if len(sys.argv) != 3:
        print("usage: file.py {--count | --topcount} file.txt")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option" + option)


if __name__ == "__main__":
    main()
