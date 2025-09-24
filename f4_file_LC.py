###########################################
# TP dev efficace semaine 1               #
# implementation file FIFO liste chaînée  #
###########################################



import unittest


class Cellule:
    def __init__(self, valeur, suivante):
        """création d'une cellule

        Args:
            valeur (quelconque): la valeur à stocker dans la cellule
            suivante (Cellule): la cellule suivante de la liste chaînée
        """
        self.valeur = valeur
        self.suivante = suivante

class File_LC:
    def __init__(self):
        """création file vide
        """

        self.entrée = None #dernier maillon de la liste, où on fait les ajouts
        self.sortie = None #premier maillon de la liste, prêt à sortir

    def est_vide(self):
        return self.sortie==None

    def ajouter(self, x):
        """ajoute x au sommet de la pile

                Args:
                    x : élément à empiler
                """
        c = Cellule(x, None)
        if self.est_vide():
            self.entrée = c
            self.sortie = c
        else:
            self.entrée.suivante = c
            self.entrée = c

    def defiler(self):
        """renvoie et supprime l'élément le plus ancien
        Raises:
            Exception : si la file est vide
        Returns:
            un élément de type quelconque
        """
        if self.est_vide():
            raise Exception("La file est vide !")
        else:
            asupprimer = self.sortie
            self.sortie = asupprimer.suivante
            return asupprimer.valeur


class TestFile(unittest.TestCase):

    def test_vide(self):
        for N in [0, 1, 2, 5, 10, 100]:
            f = File_LC()
            f.ajouter(N)
            self.assertTrue(f.est_vide())

            if N > 1:
                f.ajouter(0)
                self.assertFalse(f.est_vide())

    def test_ajouter(self):
        for N in [1, 2, 5, 10, 100]:
            f = File_LC()
            for i in range(N):
                f.ajouter(0)

    def test_defiler(self):
        f = File_LC()
        for N in [1, 2, 5, 10, 100]:
            f.ajouter(N)
            for k in range(N):
                for i in range(N):
                    f.ajouter(i)
                for i in range(N):
                    self.assertEqual(f.defiler(), i)

    def test_scenario(self):
        f = File_LC()
        self.assertTrue(f.est_vide())
        for i in range(5):
            f.ajouter(i)
            self.assertFalse(f.est_vide())
        self.assertEqual(f.defiler(), 0)
        self.assertEqual(f.defiler(), 1)
        self.assertEqual(f.defiler(), 2)


if __name__ == '__main__':
    unittest.main()

""" 
A vous d'écrire les méthodes de la file ainsi que les tests !
"""