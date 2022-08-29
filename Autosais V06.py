class Cancel(Exception):
    pass

from Composants import Conditionnement, Insert, Melange
from Coordonnées import CoordonnéesExcel
from Coordonnées import CoordonnéesEcran as CE
from Operations import Initiation
from Operations import Operation
from Configuration import Configu
from Objet_move import Move
import pyautogui as sy
from win32com.client import GetObject
import time
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
melange = [Melange]
insert = [Insert]
conditionnement = [Conditionnement]

comm_de = ['Debut']
CXl = CoordonnéesExcel(wb, 'Envoi Sylob', 'G', 'H', 'I', 'J', 'K')
CE.dictio = Configu().execute()
liste = list(CE.dictio.keys())
#gamme = move.ex_dir('Get xl', CXl.get_coordonnées())

# print("test")

Operation.set(CE.dictio, wb, CE.dictio['Operation'][0], CE.dictio['Operation sans ins'][0], CE.dictio['Operation modif'][0], CE.dictio['Operation sans ins modif'][0], CE.dictio['Commentaire'][0], CE.dictio['Espace Valider'][0], CE.dictio['Fermer'][0])
Operation.set_pause(PAUSE)

# print("test")

Initiation.set_pause(PAUSE)
#p_init = Initiation(wb1 = wb, coordonées = CE.dictio, etablissement = 'LILLE', code_article = CXl.get_coordonnées(), code = CXl.get_coordonnées(), libellé = CXl.get_coordonnées(), code_composant = CXl.get_coordonnées(), poids = CXl.get_coordonnées(), comm_composant = CXl.get_coordonnées(), gamme1 = gamme)

#print(CXl.get_itération())
while CXl.read_contenu() != False:
    match CXl.read_contenu():
        case 'infos':
            print(CXl.get_itération())
            info_gén = Initiation(wb1 = wb, coordonées = CE.dictio, etablissement = CXl.get_coordonnées(), code_article = CXl.get_coordonnées(), code = CXl.get_coordonnées(), libellé = CXl.get_coordonnées()) 
            print(info_gén.etablissement)
            print(info_gén.code_article)
            print(info_gén.code)
            print(info_gén.libellé)

        case 'mélange':
            tempMél = Melange(melange = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            melange.append(tempMél)
            #print(tempMél)

        case 'insert':
            tempIns = Insert(insert = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            insert.append(tempIns)
            #print(tempIns)

        case 'conditionnement':
            tempCon = Conditionnement(conditionnement = CXl.liste[CXl.get_itération()][1], qte =  CXl.liste[CXl.get_itération()][3], qte_pour = CXl.liste[CXl.get_itération()][4])
            conditionnement.append(tempCon)
            #print(tempCon)

        case 'opération':
            tempOpé = Operation(centre = CXl.liste[CXl.get_itération()][1], tps_reg = CXl.liste[CXl.get_itération()][2], tps_fab =  CXl.liste[CXl.get_itération()][3], commentaire = CXl.liste[CXl.get_itération()][4])
            operation.append(tempOpé)
            #print(tempOpé)
            
            

        case _:     # default
            if CXl.read_contenu() != "":
                print("problème")
 
    CXl.set_itération()

print("fin de lecture") 

for m in melange:
    print(m)

for i in insert:
    print(i)

for c in conditionnement:
    print(c)

for o in operation:
    print(o)


# Récupération effectuée



def main():
    variri = sy.confirm(text = 'Veuillez faire un choix (lors de la saisie: appuier sur échap pour arreter)"', title = 'Saisie', buttons = ['Commencer','Configurer','Annuler'])
    if variri == 'Configurer':
        CE.dictio = Configu().execute()
        coef1[0] = sy.confirm(text = 'Choisir la vitesse de saisie(inférieur à 1 ==> ++rapide)', title = 'Saisie', buttons = ['0.4','0.6','0.8','1','1.2','1.4','1.8','2'])
        coef[0] = float(coef1[0])
        Operation.set_speed(coef[0])
        Initiation.set_speed(coef[0])
        comm_de[0] = sy.confirm(text = 'Choisir un type de saisie', title = 'Saisie', buttons = ['Saisie complete','Saisie partielle','Annuler'])
        if comm_de[0] == 'Saisie partielle':
            comm_de[0] = sy.confirm(text = 'Choisir l\'étape à partir de laquelle vous voulez commencer', title = 'Operation', buttons = ['Debut','Composant','Import DT','Remplissage des ops'])
        elif comm_de[0] == 'Annuler':
            variri = comm_de[0]
        else:
            comm_de[0] = 'Debut'
    if variri == 'Annuler':
        raise Cancel
    start_time = time.time()

    # Execution

    info_gén.p_ajouter()

    for m in melange:
        m.execute()

    for i in insert:
        i.execute()

    for c in conditionnement:
        c.execute()

    for o in operation:
        o.execute()


    temps = str(time.time() - start_time)
    sy.confirm(text = temps, title = 'Fin de saisie', buttons = [
        'ok'])


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

