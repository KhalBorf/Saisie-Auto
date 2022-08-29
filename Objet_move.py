class Error(Exception):

    def __str__(self):
        return 'Arret échap par utilisateur'


import pyautogui as sy
from pynput import keyboard
import pyperclip

def type_unicode(text):
    pyperclip.copy(text)
    sy.hotkey('ctrl', 'v')


def sortir(td):
    with keyboard.Events() as events:
        event = events.get(td*Move.speed)
        if format(event) == 'Press(key=Key.esc)' or format(event) == 'Release(key=Key.esc)':
            raise Error




def taber(cclé, nnombre):
    for i in range(nnombre):
        sy.press(cclé)


class Move:
    speed = 1

    def __init__(self, wb):
        self.séquence = []
        self.wb = wb
        self.retour = ''
        
    @classmethod
    def set_speed(cls, speed):
        cls.speed = speed


    @classmethod
    def set_pause(cls, pause):
        sy.PAUSE = pause



    def definir_séquence(self, *args):
        self.séquence = []
        for s in args:
            self.séquence.append(s)


    def excecuter_séquence(self):
        for i in range(len(self.séquence)):
            if self.séquence[i] == 'Press': # Cliquer sur une touche du clavier 'tab', 'enter'
                sy.press(self.séquence[i + 1])
            if self.séquence[i] == 'Click': # Cliquer sur des coordonnées de l'écran 'Click',(x,y)
                sy.click(self.séquence[i + 1])
            if self.séquence[i] == 'Get xl': # Extraire des infos depuis l'excel 'Get xl', (Feuil, cellule)
                self.excel_get(self.séquence[i + 1])
            if self.séquence[i] == 'Paste xl': # 'Paste xl', (Feuil, cellule)
                self.excel_paste(self.séquence[i + 1], self.séquence[i + 2])
            if self.séquence[i] == 'Scroll': 
                sy.scroll(-1800)
                sortir(0.1)
            if self.séquence[i] == 'Wait': # 'Wait', 1.5
                sortir(self.séquence[i + 1])
            if self.séquence[i] == 'Type': # 'Type', 'dgdg'
                type_unicode(self.séquence[i + 1])
            if self.séquence[i] == 'Move':  
                sy.moveTo(self.séquence[i + 1])
            if self.séquence[i] == 'Taber': # 'Taber', n_click
                taber('tab', self.séquence[i + 1])
            if self.séquence[i] == 'Write': # 'Write', 'mach'
                sy.write(self.séquence[i + 1])


    def ex_dir(self, *args): # LEs 
        self.séquence = []
        for s in args:
            self.séquence.append(s)
        self.excecuter_séquence()
        return self.retour


    def excel_paste(self, coordonées, t):
        paper = coordonées[0]
        cell = coordonées[1]
        ws = self.wb.Sheets(paper)
        valeur = ws.Range(cell).Value
        type_unicode(valeur)
        sortir(t)


    def excel_get(self, coordonées):
        paper = coordonées[0]
        cell = coordonées[1]
        ws = self.wb.Sheets(paper)
        self.retour = ws.Range(cell).Value
        print(self.retour)