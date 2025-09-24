##########################################
# TP dev efficace semaine 1              #
# implementation pile par liste chaînée  #
##########################################



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



class Pile:
    def __init__(self):
        """création d'une pile vide
        """
        self.sommet = None #le haut de la pile

    def est_vide(self):
        """renvoie un booléen indiquant si la file est vide

        Returns:
            booleen
        """
        return self.sommet == None

    def empiler(self, x):
        """ajoute x au sommet de la pile

                Args:
                    x : élément à empiler
                """
        cellule = Cellule(x,self.sommet)
        self.sommet = cellule

    def depiler(self):
        """renvoie et supprime l'élément le plus ancien
        Raises:
            Exception : si la file est vide
        Returns:
            un élément de type quelconque
        """
        if self.est_vide():
            raise Exception("La pile est vide !")
        else:
            x = self.sommet
            self.sommet = self.sommet.suivante
            return x.valeur

class TestPile(unittest.TestCase):

    def test_vide(self):
        p = Pile()
        self.assertTrue(p.est_vide())

    def test_empiler(self):
        for N in [0, 1, 2, 5, 10, 100]:
            p = Pile()
            for i in range(N):
                p.empiler(i)
                self.assertEqual(p.sommet.valeur, i)



    def test_depiler(self):
        for N in [0, 1, 2, 5, 10, 100]:
            p = Pile()
            with self.assertRaises(BaseException):
                p.depiler(0)
            for i in range(N // 2):
                p.empiler(i)
            for i in range(N // 2):
                self.assertEqual(p.depiler(), N // 2 - 1 - i)

    def test_scenario_complet(self):
        p = Pile()
        self.assertTrue(p.est_vide())
        for i in range(5):
            p.empiler(i)
        self.assertEqual(p.depiler(), 4)
        self.assertEqual(p.depiler(), 3)
        self.assertEqual(p.depiler(), 2)
        p.empiler(5)
        p.empiler(6)
        self.assertEqual(p.depiler(), 6)
        self.assertEqual(p.depiler(), 5)
        self.assertEqual(p.depiler(), 1)
        self.assertEqual(p.depiler(), 0)
        with self.assertRaises(BaseException):
            p.depiler()



if __name__ == '__main__':
    unittest.main()

""" 
A vous d'écrire les méthodes de la pile ainsi que les tests !
"""