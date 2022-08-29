class Cancel(Exception):
    pass

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
        wb = xl.Workbooks('Convertisseur DT Sylob.xlsm')
        break
    except:
        if sy.confirm(text ='Veuillez ouvrir l\'excel du génerateur de données', title = 'Alert', buttons = ['C\'est fait','Arreter']) != 'C\'est fait':
            exit(0)


PAUSE = 0
move = Move(wb)
coef1 = [0]
coef = [0]
comm_de = ['Debut']
CXl = CoordonnéesExcel(wb, 'Valeurs Sylob', 'D', 'E')
CE.dictio = Configu().execute()
liste = list(CE.dictio.keys())
gamme = move.ex_dir('Get xl', CXl.get_coordonnées())


Operation.set(CE.dictio, wb, CE.dictio['Operation'][0], CE.dictio['Operation sans ins'][0], CE.dictio['Operation modif'][0], CE.dictio['Operation sans ins modif'][0], CE.dictio['Commentaire'][0], gamme, CE.dictio['Espace Valider'][0], CE.dictio['Fermer'][0])
Operation.set_pause(PAUSE)



Initiation.set_pause(PAUSE)
p_init = Initiation(wb1 = wb, coordonées = CE.dictio, etablissement = 'CHERBOURG', code_article = CXl.get_coordonnées(), code = CXl.get_coordonnées(), libellé = CXl.get_coordonnées(), code_composant = CXl.get_coordonnées(), poids = CXl.get_coordonnées(), comm_composant = CXl.get_coordonnées(), gamme1 = gamme)

info_gén = Operation(commentaire = CXl.get_coordonnées())
prépa_MP = Operation(commentaire = CXl.get_coordonnées())
prépa_ins = Operation(commentaire = CXl.get_coordonnées())
réglage = Operation(centre = CXl.get_coordonnées(), tps_reg = CXl.get_coordonnées(), commentaire = CXl.get_coordonnées())
moulage = Operation(centre = CXl.get_coordonnées(), tps_fab = CXl.get_coordonnées())
finition = Operation(tps_reg = CXl.get_coordonnées(), tps_fab = CXl.get_coordonnées(), commentaire = CXl.get_coordonnées())
emballage = Operation(commentaire = CXl.get_coordonnées())

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
    if comm_de[0] == 'Debut':
        p_init.p_ajouter()
        p_init.composant()
        p_init.DonnT()
    elif comm_de[0] == 'Composant':
        p_init.composant()
        p_init.DonnT()
    elif comm_de[0] == 'Import DT':
        p_init.DonnT()
    if gamme == 'INSERT':
        info_gén.execute()
        prépa_MP.execute()
        prépa_ins.execute()
    else:
        info_gén.execute()
        prépa_MP.execute()
    # p_init.p_ajouter()
    # p_init.composant()
    # p_init.DonnT()
    # info_gén.execute()
    # prépa_MP.execute()
    réglage.execute()
    moulage.execute()
    finition.execute()
    emballage.execute()
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
            if sy.confirm(text='Saisie annulé', title='Alert', buttons=['Refaire', 'Arreter']) == 'Refaire':
                mains()
            else:
                exit(0)

mains()