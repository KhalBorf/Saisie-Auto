class Cancel(Exception):
    pass

from Composants import Composants
from Coordonnées import CoordonnéesExcel
from Coordonnées import CoordonnéesEcran as CE
from Operations import Initiation
from Operations import Operation
from Configuration import Configu
from Objet_move import Move
import pyautogui as sy
import sys
from win32com.client import GetObject
import time


#while(True): # test récupération couleur
    #print(PIL.ImageGrab.grab().load()[100,100])


while(True):
    try:
        xl = GetObject(None, 'Excel.Application')
        wb = xl.Workbooks('récupération données techniques access.xlsb')
        break
    except:
        if sy.confirm(text ='Veuillez ouvrir l\'excel du génerateur de données', title = 'Alert', buttons = ['C\'est fait','Arreter']) != 'C\'est fait':
            exit(0)


PAUSE = 0
move = Move(wb)
coef1 = [0]
coef = [0]

operation = [Operation]
composants = [Composants]

comm_de = ['Debut']
CXl = CoordonnéesExcel(wb, 'Envoi Sylob', 'G', 'H', 'I', 'J', 'K')
CE.dictio, fin = Configu().execute()
if fin == -1:
    sys.exit()
 
liste = list(CE.dictio.keys())
#gamme = move.ex_dir('Get xl', CXl.get_coordonnées())

Operation.set(CE.dictio, wb, CE.dictio['Dossier'][0], CE.dictio['Operation'][0], CE.dictio['Commentaire Operation'][0], CE.dictio['Fenetre Operation'])
Operation.set_pause(PAUSE)

Composants.set(CE.dictio, wb, CE.dictio['Dossier'][0], CE.dictio['Composant'][0], CE.dictio['Fenetre Composant'])
Composants.set_pause(PAUSE)

Initiation.set_pause(PAUSE)                                                                           	                                                                                    

#p_init = Initiation(wb1 = wb, coordonées = CE.dictio, etablissement = 'LILLE', code_article = CXl.get_coordonnées(), code = CXl.get_coordonnées(), libellé = CXl.get_coordonnées(), code_composant = CXl.get_coordonnées(), poids = CXl.get_coordonnées(), comm_composant = CXl.get_coordonnées(), gamme1 = gamme)

#print(CXl.get_itération())
while CXl.read_contenu() != False:
    match CXl.read_contenu():
        case 'infos':
            info_gén = Initiation(wb1 = wb, coordonées = CE.dictio, code_article = CXl.get_coordonnées(), etablissement = CXl.get_coordonnées(), code = CXl.get_coordonnées(), libellé = CXl.get_coordonnées()) 
            #print(info_gén.etablissement) #! La valeur de Lille est mise automatiquement vu que les menus déroulants ne veulent pas de ^V                                   

        case 'mélange':
            tempCom = Composants("Mélange", code = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            composants.append(tempCom)

        case 'insert':
            tempCom = Composants("Insert", code = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            composants.append(tempCom)

        case 'conditionnement':
            tempCom = Composants("Conditionnement", code = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            composants.append(tempCom)

        case 'opération': # Le 3 et le 2 sont inversé avec le "Quantité (Pour)" dans l'Excel qui est à gauche et qui doit être rentré à droite 
            tempOpé = Operation(centre = CXl.liste[CXl.get_itération()][1], tps_reg = CXl.liste[CXl.get_itération()][3], tps_fab =  CXl.liste[CXl.get_itération()][4], commentaire = CXl.liste[CXl.get_itération()][2])
            operation.append(tempOpé)
            

        case _:     # default
            if CXl.read_contenu() != "":
                print("problème")
 
    CXl.set_itération()

print("fin de lecture") 

"""
for o in operation:
    print(o)


for c in composants:
    print(c)
"""
# Récupération effectuée



def main():
    val = sy.confirm(text = 'Veuillez faire un choix (lors de la saisie: appuier sur échap pour arreter)"', title = 'Saisie', buttons = ['Commencer','Configurer','Annuler'])
    if val == 'Configurer':
        CE.dictio, fin = Configu().execute()
        print(fin)
        if fin == -1:
            sys.exit()
        coef1[0] = sy.confirm(text = 'Choisir la vitesse de saisie(inférieur à 1 ==> ++rapide)', title = 'Saisie', buttons = ['0.4','0.6','0.8','1','1.2','1.4','1.8','2'])
        coef[0] = float(coef1[0])
        Operation.set_speed(coef[0])
        Initiation.set_speed(coef[0])
        Composants.set_speed(coef[0])
        comm_de[0] = 'Debut'
    if val == 'Annuler':
        raise Cancel
    start_time = time.time()

    # Execution
    
   

    info_gén.p_ajouter()

    for o in operation:     #! L'opération 0 n'existe pas !! 
        if o != operation[0]:
            o.i[1] = o.centre
            if str(o.move.ex_dir('Get xl', o.i))[0] != 'A': # Si l'opération est un plateaux --> on le passe en composants
                o.execute()
            else:
                composants.append(Composants("Plateaux", code = o.centre, qte =  o.tps_fab, qte_pour = o.tps_reg)) #On échange les quantitées
         
    # OK



    precedent = ""          # Si le type du composant d'avant est le même que ce composant, on ne change pas l'opération
    for c in composants:    #! Le composant 0 n'existe pas !! 
        if c != composants[0]:
            res = 0
            res = c.execute(precedent)
            if res != -1:
                precedent = c.type
    
    # OK

    temps = time.time() - start_time
    sy.confirm(text = ' Temps du transfert : ' + str(round(temps,3)) + ' secondes', title = 'Fin de saisie', buttons = [
        'ok'])

    # OK

    for c in composants:
        if c != composants[0]:
            if c.type == "Plateaux":
                composants.remove(c)

#for c in composants:
#    print(c)

def mains():
    try:
        main()
        if sy.confirm(text = 'Fin de saisie', title = 'Alert', buttons = ['Suivant', 'Arreter']) == 'Suivant':
            mains()
        else:
            exit(0)
    except Exception as e:
        name =  type(e).__name__
        if name == "Cancel" or name == "Error":
            if sy.confirm(text='Saisie annulée', title='Alert', buttons=['Refaire', 'Arreter']) == 'Refaire':
                mains()
            else:
                exit(0)

mains()

