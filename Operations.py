from this import d
from tkinter import E
from xmlrpc.client import Boolean
from Objet_move import Move
from pynput.keyboard import Key, Controller
import pyautogui as sy
import PIL.ImageGrab
class Initiation:

    def __init__(self, wb1, coordonées, etablissement, code_article, code, libellé):
        self.move = Move(wb1)
        self.i = [0,0]
        self.c_ajouter2 = [0,0]
        self.c_ajouter3 = [0,0]
        liste = list(coordonées.keys())

        self.c_ajouter = coordonées[liste[0]][0]
        self.c_ajouter2[0] = self.c_ajouter[0]
        self.c_ajouter2[1] = self.c_ajouter[1] + 22
        self.c_ajouter3[0] = self.c_ajouter[0] 
        self.c_ajouter3[1] = self.c_ajouter[1] - 22

        self.c_fenetre = coordonées[liste[1]][0]

        self.etablissement = self.move.ex_dir('Get xl', etablissement)
        self.code_article = code_article
        self.code = code
        self.libellé = libellé

    def p_ajouter(self): # bon

        self.move.ex_dir('Wait', 1, 'Click', self.c_ajouter, 'Click', self.c_ajouter2, 'Click', self.c_ajouter3, 'Wait', 1) # On clique au cas ou il y a eu une suppression
        
        # Récupération de la couleur en c_fenetre

        couleur = PIL.ImageGrab.grab().load()[self.c_fenetre[0], self.c_fenetre[1]]

        self.move.ex_dir('Taber', 1, 'Press', 'enter')

        # Tant que la couleur est la même, on ne continue pas
        tps = 0
        while couleur == PIL.ImageGrab.grab().load()[self.c_fenetre[0], self.c_fenetre[1]]:
            self.move.ex_dir('Wait', 0.1)


        self.move.ex_dir('Wait', 0.2, 'Taber', 4,'Press', 'enter', 'Wait', 0.5, 'Press 2', 'alt', 'r' , 'Wait', 4,
                         'Taber', 7, 'Write', 'Ancien', 'Taber', 2, 'Wait', 0.5, 'Paste xl', self.code_article, 0.2,
                         'Wait', 0.2, 'Taber', 41, 'Wait', 0.2, 'Press', 'enter')
       
        sy.confirm(text = 'Sélectionnez l\'article PUIS appuyez sur OK', title = 'Saisie', buttons = ['OK'])

        self.move.ex_dir('Wait', 0.5,'Taber', 4, 'Wait', 0.2, 'Press', self.etablissement[0], 'Press', self.etablissement[1], 'Press', self.etablissement[2], 'Press', self.etablissement[3],
                         'Wait', 0.5, 'Taber', 7, 'Paste xl', self.code, 0.2, 'Taber', 1, 'Paste xl', self.libellé, 0.2, 'Wait', 0.4, 
                         'Press 2','alt', 'v', 'Wait', 0.2, 'Press', 'Enter')


    def set_pause(pause):
        Move.set_pause(pause)


    def set_speed(speed):
        Move.set_speed(speed)


class Operation:
    itération = 0
    premièreop = (0, 0)
    wb = 0
    dossier = 0
    op1 = 0
    c_comm = 0
    coordonées = 0
    existe = (Boolean)
    i = [0,0]

    def __init__(self, centre=False, tps_reg=False, tps_fab=False, commentaire = False):
        self.move = Move(Operation.wb)
        self.itérer()
        self.ordre = Operation.itération
        self.centre = centre
        self.tps_fab = tps_fab
        self.tps_reg = tps_reg
        self.commentaire = commentaire
        self.l = [0,0]
        self.existe = True
        self.tabulations = {
            'Centre de charge': 5,
            'CC<>reglage': 23,
            'Reglage<>fab': 7 }
        self.liste = list(self.tabulations)

    def set_pause(pause):
        Move.set_pause(pause)


    def set_speed(speed):
        Move.set_speed(speed)

    @classmethod
    def itérer(cls):
        cls.itération += 1

    @classmethod
    def set(cls, coordonées, wb, dossier, op1, c_comm, f_op):
        cls.coordonées = coordonées
        cls.wb = wb
        cls.dossier = dossier
        cls.op1 = op1
        cls.c_comm = c_comm
        cls.f_op = f_op

    def execute(self):
        if self.ordre == 1:
            self.opération1() # bon  
        if self.centre != None and self.existe == True:
            self.p_centre()   # bon
        if self.tps_reg != None and self.existe == True:
            self.temps_reg()  # bon
        if self.tps_fab != None and self.existe == True:
            self.temps_fab()  # bon
        if self.commentaire != None and self.existe == True:
            self.p_commentaire()    # bon
        if Operation.itération == self.ordre and self.existe == True:
            self.fermer()     # bon
        elif self.existe == True:
            self.valider()    # bon
        elif Operation.itération == self.ordre:
            self.annuler()    # bon



    def p_centre(self): 
        self.i[1] = self.centre

        c = str(self.move.ex_dir('Get xl', self.i))
        couleur = PIL.ImageGrab.grab().load()[Operation.f_op[0][0], Operation.f_op[0][1] + 18]   
        self.move.ex_dir('Wait', 0.2, 'Paste xl', self.i, 0.2)
        tps = 0
        while couleur == PIL.ImageGrab.grab().load()[Operation.f_op[0][0], Operation.f_op[0][1] + 18 ] and tps < 1.5:
            self.move.ex_dir('Wait', 0.1)
            tps+= 0.1
        if tps >= 1.5: # Le centre de charge n'existe pas

            self.existe = False
            kb = Controller()
            for loop in range(len(c)):
                kb.press(Key.backspace)
                kb.release(Key.backspace)
                
        else:
            self.move.ex_dir('Wait', 0.2, 'Press', 'enter', 'Wait', 0.6)

        self.l[0] = 1


    def temps_reg(self):
        if self.l[0] == 1:
            ta = self.tabulations[self.liste[1]]
        else:
            ta = self.tabulations[self.liste[1]] + self.tabulations[self.liste[0]]
        self.temps(self.tps_reg, ta, 24)
        self.l[1] = 1


    def temps_fab(self):
        if self.l[1] == 1:
            ta = self.tabulations[self.liste[2]]
        elif self.l[0] == 1:
            ta = self.tabulations[self.liste[2]] + self.tabulations[self.liste[1]] - 1
        else:
            ta = self.tabulations[self.liste[2]] + self.tabulations[self.liste[1]] + self.tabulations[self.liste[0]]
        self.temps(self.tps_fab, ta, 1)


    def p_commentaire(self):
        self.i[1] = self.commentaire
        if self.move.ex_dir('Get xl', self.i)!= None:
            self.move.ex_dir('Wait', 0.1, 'Move', (960, 540), 'Scroll', 'Wait', 0.4, 'Click', Operation.c_comm, 'Press', 'Enter', 'Paste xl', self.i, 0.1, 'Wait', 0.1)


    def temps(self, trx, ta, tb):
        self.i[1] = trx
        trx1 = self.move.ex_dir('Get xl', self.i)
        if trx1 != None:
            if tb!=1:
                strx = trx1*tb
                if strx < 0.0167 and strx != 0: # On met 1min si c'est en dessous de 1min
                    strx = 0.0167
            else:
                strx = 60 / trx1 / 60
                if strx < 0.0003 and strx != 0: # On met 1sec si c'est en dessous de 1sec
                    strx = 0.0003

            self.move.ex_dir('Taber', ta, 'Press', 'enter', 'Wait', 0.3, 'Type', strx, 'Taber', 1, 'Press', 'enter', 'Wait', 0.3)
        else:
            self.move.ex_dir('Taber', ta)


    def valider(self):      # 100% bon
        self.move.ex_dir('Press 2', 'alt', 'n', 'Wait', 0.4)


    def opération1(self):   # 100% bon

        t = Operation.dossier
        f = Operation.op1
        self.move.ex_dir('Scroll Up', 'Wait', 0.2, -900, 'Click', t, 'Wait', 0.2, 'Click', f , 'Wait', 0.4)


    def fermer(self):
        self.move.ex_dir('Wait', 0.4, 'Press 2', 'alt', 'v', 'Wait', 0.4)

    def annuler(self):
        self.move.ex_dir('Wait', 0.4, 'Press 2', 'alt', 'a', 'Wait', 0.4, 'Press', 'enter', 'Wait', 0.4)

    def __str__(self):
        return "Cdc : " + self.centre + "\nTps Réglage : " + self.tps_reg + "\nTps Fab. : " + self.tps_fab + "\nCommentaire : " + self.commentaire + "\n\n"