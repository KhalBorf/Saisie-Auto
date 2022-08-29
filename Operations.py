gammes = [
    'INSERT',
    'NON']
from Objet_move import Move

class Initiation:

    def __init__(self, wb1, coordonées, etablissement, code_article, code, libellé, code_composant, poids, comm_composant, gamme1):
        self.move = Move(wb1)
        liste = list(coordonées.keys())
        self.c_ajouter = coordonées[liste[0]][0]
        self.c_dossier = coordonées[liste[1]][0]
        self.c_composant = coordonées[liste[2]][0]
        self.c_dossier2 = coordonées[liste[3]][0]
        self.c_mdt = coordonées[liste[4]][0]
        self.c_sinsert = coordonées[liste[5]][0]
        self.c_insert = coordonées[liste[6]][0]
        self.c_valider = coordonées[liste[13]][0]
        self.code_article = code_article
        self.etablissement = etablissement
        self.code = code
        self.libellé = libellé
        self.code_composant = code_composant
        self.poids = poids
        self.comm_composant = comm_composant
        self.gamme = gamme1


    def p_ajouter(self):
        self.move.ex_dir('Wait',1,'Click', self.c_ajouter ,'Taber', 1, 'Press', 'enter', 'Wait', 0.2, 'Paste xl', self.code_article, 0.2,
                         'Taber', 1, 'Wait', 0.2, 'Taber', 4, 'Press', 'enter', 'Write', self.etablissement,'Press', 'enter',
                         'Wait', 0.2, 'Taber', 7, 'Paste xl', self.code, 0.2, 'Taber', 1, 'Paste xl', self.libellé, 0.2, 'Taber', 2,'Press', 'Enter',
                         'Wait', 0.4)



    def composant(self):# à modifier
        self.move.ex_dir('Click', (960,540), 'Scroll', 'Wait', 0.2, 'Click', self.c_dossier, 'Wait', 0.2,'Scroll', 'Wait', 0.2,
                         'Click', self.c_composant, 'Wait', 0.3, 'Paste xl', self.code_composant, 0.2, 'Taber', 1, 'Wait', 0.3,
                         'Paste xl', self.poids, 0.3, 'Taber', 12, 'Paste xl', self.comm_composant, 0.1,'Taber', 3, 'Wait', 0.3, 'Press', 'enter')


    def DonnT(self):# à modifier
        self.move.ex_dir('Click', (960, 540), 'Scroll', 'Wait', 0.2, 'Click', self.c_dossier2, 'Wait', 0.1, 'Scroll', 'Wait', 0.3, 'Click', self.c_mdt, 'Wait', 1)
        if self.gamme == gammes[0]:
            self.move.ex_dir('Click', self.c_insert)
        else:
            self.move.ex_dir('Click', self.c_sinsert)
        self.move.ex_dir('Wait', 0.5, 'Press', 'enter', 'Wait', 1.5)


    def set_pause(pause):
        Move.set_pause(pause)


    def set_speed(speed):
        Move.set_speed(speed)



class Operation:
    itération = 0
    premièreop = (0, 0)
    gamme = ('', '')
    wb = 0
    op1 = 0
    op2 = 0
    opm1 = 0
    opm2 = 0
    c_comm = 0
    gamme = 0
    fermer = 0
    coordonées = 0
    c_valider = (0, 0)
    c_fermer = (0, 0)

    def __init__(self, centre=False, tps_reg=False, tps_fab=False, commentaire = False):
        self.move = Move(Operation.wb)
        self.itérer()
        self.ordre = Operation.itération
        self.centre = centre
        self.tps_fab = tps_fab
        self.tps_reg = tps_reg
        self.commentaire = commentaire
        self.l = [0,0]
        self.tabulations = {
            'Centre de charge': 5,
            'CC<>reglage': 18,
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
    def set(cls, coordonées, wb, op1, op2, opm1, opm2, c_comm, gamme, c_valider, c_fermer):
        cls.coordonées = coordonées
        cls.wb = wb
        cls.op1 = op1
        cls.op2 = op2
        cls.opm1 = opm1
        cls.opm2 = opm2
        cls.c_comm = c_comm
        cls.gamme = gamme
        cls.c_valider = c_valider
        cls.c_fermer = c_fermer

    def execute(self):
        if self.ordre == 1:
            self.opération1()
        if self.centre:
            self.p_centre()
        if self.tps_reg:
            self.temps_reg()
        if self.tps_fab:
            self.temps_fab()
        if self.commentaire:
            self.p_commentaire()
        else:
            self.move.ex_dir('Scroll', 'Wait', 0.4)
        if Operation.itération == self.ordre:
            self.valider(1)
            self.fermer()
        else:
            self.valider(0)


    def p_centre(self): # à modifier si apres operation modele
        self.move.ex_dir('Taber', self.tabulations[self.liste[0]], 'Paste xl', self.centre, 0.1)
        self.l[0] = 1


    def temps_reg(self): # à modifier
        if self.l[0] == 1:
            ta = self.tabulations[self.liste[1]]
        else:
            ta = self.tabulations[self.liste[1]] + self.tabulations[self.liste[0]]
        self.temps(self.tps_reg, ta)
        self.l[1] = 1


    def temps_fab(self): # à modifier
        if self.l[1] == 1:
            ta = self.tabulations[self.liste[2]]
        elif self.l[0] == 1:
            ta = self.tabulations[self.liste[2]] + self.tabulations[self.liste[1]] -1
        else:
            ta = self.tabulations[self.liste[2]] + self.tabulations[self.liste[1]] + self.tabulations[self.liste[0]]
        self.temps(self.tps_fab, ta)


    def p_commentaire(self):
        self.move.ex_dir('Wait', 0.1, 'Move', (960, 540), 'Scroll', 'Wait', 0.4, 'Click', Operation.c_comm, 'Paste xl', self.commentaire, 0.1, 'Wait', 0.1)


    def temps(self, trx, ta):
        trx1 = self.move.ex_dir('Get xl', trx)
        strx = str(trx1)
        self.move.ex_dir('Taber', ta, 'Press', 'enter', 'Wait', 0.3, 'Type', strx, 'Press', 'tab', 'Press', 'enter', 'Wait', 0.3)


    def valider(self, ta):
        self.move.ex_dir('Click', self.c_valider, 'Taber', 3 - ta, 'Press', 'enter', 'Wait', 0.4)


    def opération1(self):# à modifier
        t = 0
        f = 0
        if Operation.gamme == gammes[0]:
            t = Operation.opm1
            f = Operation.op1
        else:
            t = Operation.opm2
            f = Operation.op2
        self.move.ex_dir('Scroll', 'Wait', 0.2, -900, 'Click', f, 'Wait', 0.2, 'Click', t, 'Wait', 0.4)


    def fermer(self):
        self.move.ex_dir('Scroll', 'Wait', 0.1, 'Click', Operation.c_fermer)