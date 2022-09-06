from ast import Str
from pickle import FALSE
from re import S
from webbrowser import Opera
from Objet_move import Move
from pynput.keyboard import Key, Controller
import PIL.ImageGrab

class Composants:

    itération = 0
    c_dossier2 = [0, 0]
    c_composants = [0, 0]
    wb = 0
    coordonées = 0
    i = [0,0]

    def __init__(self, type, code=FALSE, qte=FALSE, qte_pour=FALSE):
        
        self.move = Move(Composants.wb)
        self.itérer()
        self.ordre = Composants.itération
        self.type = type
        self.code = code
        self.qte = qte
        self.qte_pour = qte_pour
        self.existe = True

    def set_pause(pause):
        Move.set_pause(pause)


    def set_speed(speed):
        Move.set_speed(speed)

    @classmethod
    def itérer(cls):
        cls.itération += 1

    @classmethod
    def set(cls, coordonées, wb, c_dossier, c_composants, f_comp):
        cls.coordonées = coordonées
        cls.wb = wb
        cls.c_dossier2[0] = c_dossier[0]
        cls.c_dossier2[1] = c_dossier[1]
        cls.c_dossier2[0] = cls.c_dossier2[0] + 30 # On sélectionne l'opération en dessous du dossier 
        cls.c_dossier2[1] = cls.c_dossier2[1] + 18
        cls.c_composants = c_composants
        cls.f_comp = f_comp


    def execute(self, precedent):
        if self.ordre == 1:
            self.allerComposants()
        self.entrerArticle()
        if (precedent != self.type or precedent == "") and self.existe == True:
            self.changerOpération()
        if self.existe == True:
            self.insererQuantitées()
        if Composants.itération == self.ordre:
            self.fermer()
        elif self.existe == True:
            self.valider()
        elif Composants.itération == self.ordre:
            self.annuler()
        else:
            return -1


    def allerComposants(self):
        self.move.ex_dir('Click', Composants.c_dossier2, 'Wait' , 0.2, 'Click', Composants.c_composants, 'Wait', 0.3)

    @classmethod    
    def test(self, t):
        t = t+1

    def entrerArticle(self):
        
        self.i[1] = self.code
        c = str(self.move.ex_dir('Get xl', self.i))
        if c != None:
            tps = 0
            couleur = PIL.ImageGrab.grab().load()[Composants.f_comp[0][0],Composants.f_comp[0][1] + 18]   
            self.move.ex_dir('Paste xl', self.i, 0.2)
            while couleur == PIL.ImageGrab.grab().load()[Composants.f_comp[0][0], Composants.f_comp[0][1] + 18] and tps < 2:
                self.move.ex_dir('Wait', 0.1)
                tps+= 0.1
            
            if tps >= 2:
                self.existe = False
                kb = Controller()
                for loop in range(len(c)):
                    kb.press(Key.backspace)
                    kb.release(Key.backspace)
            else:
                self.move.ex_dir('Wait', 0.1, 'Press', 'Enter', 'Wait', 0.5, 'Press', 'Enter', 'Wait', 0.5)

    def changerOpération(self):

        
        if self.type == "Plateaux":
            self.remonter()
            self.remonter()
            self.move.ex_dir("Press", "e", "Press", "x", "Press", "t", "Press", "r", "Press", "u", 'Wait', 0.2, 'Taber', 2)
        elif self.type == "Insert":
            self.remonter()
            self.remonter()
            self.move.ex_dir(   "Press", "c", "Press", "o", "Press", "n", "Press", "d", "Press", "i", 'Wait', 1, 
                                "Press", "r", "Press", "u", "Press", "t", "Press", "i", "Press", "l", 'Wait', 1,
                                "Press", "p", "Press", "r", "Press", "e", "Press", "s", "Press", "s", "Press", "e", 'Wait', 1,
                                "Press", "p", "Press", "r", "Press", "é", "Press", "p", "Press", "a", "Press", "r", "Press", "a", "Press", "t", "Press", "i", "Press", "o", "Press", "n", 'Wait', 1,
                                "Press", "p", "Press", "r", "Press", "é", "Press", "p", "Press", "a", "Press", "r", "Press", "a", "Press", "t", "Press", "i", "Press", "o", "Press", "n", "Press", " ", "Press", "i", "Press", "n", "Press", "s", "Press", "e", "Press", "r", 'Wait', 0.2, 'Taber', 2, 'Wait', 0.2)
        elif self.type == "Conditionnement":
            self.remonter()
            self.remonter()
            self.move.ex_dir("Press", "c", "Press", "o", "Press", "n", "Press", "d", "Press", "i", 'Wait', 0.2, 'Taber', 2)



    def insererQuantitées(self):

        self.move.ex_dir('Wait', 0.4)
        qte2 = ""
        self.i[1] = self.qte

        if self.move.ex_dir('Get xl', self.i)!= None:
            temp = str(self.move.ex_dir('Get xl', self.i))
            j=0

            while temp[j] == ' ':
                j=j+1

            while j < len(temp) and temp[j] != ' ':
                qte2 = qte2 + temp[j]
                j=j+1

        self.move.ex_dir('Type', qte2, 'Wait', 0.2)

        qte2 = ""
        self.i[1] = self.qte_pour
        if self.move.ex_dir('Get xl', self.i)!= None:
            temp = str(self.move.ex_dir('Get xl', self.i))
            j=0
            while temp[j] == ' ':
                j=j+1

            while j < len(temp) and temp[j] != ' ':
                qte2 = qte2 + temp[j]
                j=j+1

            self.move.ex_dir('Taber', 1, 'Type', qte2, 'Wait', 0.2)



    def remonter(self): # 100% bon
        self.move.ex_dir('Press 2', 'shift', 'tab', 'Wait', 0.2)

    def valider(self):  # 100% bon
        self.move.ex_dir('Press 2', 'alt', 'n', 'Wait', 0.4)

    def fermer(self):   # 100% bon
        self.move.ex_dir('Wait', 0.4, 'Press 2', 'alt', 'v', 'Wait', 0.4)

    def annuler(self):   # 100% bon
        self.move.ex_dir('Wait', 0.4, 'Press 2', 'alt', 'a', 'Wait', 0.4, 'Press', 'enter', 'Wait', 0.4)

    def __str__(self):
        return "Type : " + self.type +  "\n\tCode : " + self.code + "\n\tQuantité : " + self.qte + "\n\tQuantité pour : " + self.qte_pour + "\n\n"



