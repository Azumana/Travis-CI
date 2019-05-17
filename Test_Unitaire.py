from math import pi,sqrt
import requests

def exercice_1(a, b):
    """
    Ecrire une fonction qui renvoie le produit des deux élèments
    a et b
    """
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    else:
        raise TypeError

def exercice_2(x, a, b):
    """
    Ecrire une fonction qui renvoie :
        -255 si x<a
        x si a<x<b
        255 si x>b
    (A faire en TDD)
    """
    if a>b:
        raise ValueError
    if x<a:
        return -255
    elif x>b:
        return 255
    else:
        return x


class Exercice_3:
    """
    Ecrire une classe qui renvoie des informations sur un cercle
    """

    def __init__(self):
        self.r = r

    def aire(self):
        """
        Ecrire une fonction qui renvoie l'aire d'un disque de rayon r
        """
        return pi*(r*r)

    def perimetre(self):
        """
        Ecrire une fonction qui renvoie le perimètre d'un cercle de rayon r
        """
        pass

    def dans_cercle(self, x, y):
        """
        Ecrire une fonction qui renvoie True si le point (x, y) est dans
        le cercle de r et de centre (0, 0)
        """
        pass

class Exercice_4:

    def __init__(self, lieu):
        self.lieu = lieu
        url = "https://fr.wikipedia.org/w/api.php"
        par = {
            "search": lieu,
            "format": "json",
            "action": "opensearch",
        }
        self.req = requests.get(url, params=par).json()

    def loc(self):
        return f"Voici ce que je connais de {self.lieu} : {self.req[2][0]}"

if __name__ == "__main__":
    ex = Exercice_4("Lyon")
    print(ex.loc())

