from pickle import FALSE
from Objet_move import Move

class Melange:

    def __init__(self, melange=FALSE, qte=FALSE, qte_pour=FALSE):
        self.melange = melange
        self.qte = qte
        self.qte_pour = qte_pour




    def __str__(self):
        return "Melange : " + self.melange + "\nQuantité : " + self.qte + "\nQuantité pour : " + self.qte_pour + "\n\n"




class Insert:

    def __init__(self, insert=FALSE, qte=FALSE, qte_pour=FALSE):
        self.insert = insert
        self.qte = qte
        self.qte_pour = qte_pour




    def __str__(self):
        return "Insert : " + self.insert + "\nQuantité : " + self.qte + "\nQuantité pour : " + self.qte_pour + "\n\n"



class Conditionnement:

    def __init__(self, conditionnement=FALSE, qte=FALSE, qte_pour=FALSE):
        self.conditionnement = conditionnement
        self.qte = qte
        self.qte_pour = qte_pour




    def __str__(self):
        return "Conditionnement : " + self.conditionnement + "\nQuantité : " + self.qte + "\nQuantité pour : " + self.qte_pour + "\n\n"