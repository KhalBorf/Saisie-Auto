class CoordonnéesExcel:

    def __init__(self, fichier, feuille, celulle1, celulle2, celulle3, celulle4, celulle5):
        self.feuille = feuille
        self.celulle1 = celulle1        # colonne n°1
        self.celulle2 = celulle2        # colonne n°2
        self.celulle3 = celulle3        # colonne n°3
        self.celulle4 = celulle4        # colonne n°4
        self.celulle5 = celulle5        # colonne n°5
        self.fichier = fichier
        self.ws = fichier.Sheets(feuille)
        self.liste = []
        self.itération = -1
        i = 2                          # On démarre par la ligne 2
        while self.ws.Range(self.celulle1 + str(i)).Value != None:  # On parcoure tant que ce n'est pas vide // R1 puis R2 puis R3 ....
            self.liste.append([                                     # On incrémente dans le tableau
                self.ws.Range(self.celulle1 + str(i)).Value,        # Valeur à gauche   ==> TYPE
                self.ws.Range(self.celulle2 + str(i)).Value,        #                   ==> DÉSIGNATION ou INFO GÉNÉRALE (CELLULE)
                self.ws.Range(self.celulle3 + str(i)).Value,        # Valeur au milieu  ==> COMMENTAIRE
                self.ws.Range(self.celulle4 + str(i)).Value,        #                   ==> QTE (CELLULE)
                self.ws.Range(self.celulle5 + str(i)).Value])       # Valeur à droite   ==> QTE POUR (CELLULE)
            i += 1
        print(len(self.liste))

    def get_coordonnées(self):
        #print(self.liste[0])
        try:
            self.set_itération()
            c = self.liste[self.itération]
            
        except:
            print('Erreur: Le nombre maximum de coordonnées est atteint')
            c = False
        finally:
            #print(c)
            return c

    def read_contenu(self):
        #print(self.itération)
        try:
            if(self.itération == -1):
                c = self.liste[0][0]
            else:
                c = self.liste[self.itération][0]
        except:
            print('Erreur: Le nombre maximum de coordonnées est atteint')
            c = False
        finally:
            return c

    def getCell1(self):
        return self.celulle1

    def getCell2(self):
        return self.celulle2

    def getCell3(self):
        return self.celulle3

    def getCell4(self):
        return self.celulle4

    def getCell5(self):
        return self.celulle5

    def get_tout(self):
        return self.liste

    def set_itération(self):
        self.itération += 1

    def get_itération(self):
        return self.itération

class CoordonnéesEcran:
    profile = [
        'Edouard']
    dictio = {
        'Espace ajouter': [
            (0, 0),
            [
                'Dans l\'activité: gérer les données techniques placez-vous sur: l\'espace blanc à droite du bouton ajouter, cliquez sur échap pour enregistrer']],
        'Dossier': [
            (0, 0),
            [
                'Basculez au bas de la page et placez-vous sur le dossier, cliquez sur échap pour enregistrer']],
        'Composant': [
            (0, 0),
            [
                'Basculez au bas de la page et Cliquez sur le dossier et placez-vous sur: ajouter un composant, cliquez sur échap pour enregistrer']],
        'Dossier2': [
            (0, 0),
            [
                'Apres le rajout de composant, basculez au bas de la page et placez-vous sur le dossier, cliquez sur échap pour enregistrer']],
        'ChoixDt': [
            (0, 0),
            [
                'Basculez au bas de la page et Cliquez sur le dossier et placez-vous sur: importer des DT, cliquez sur échap pour enregistrer']],
        'Sans Insert': [
            (0, 0),
            [
                'Au niveau du rajout de modele de DT placez-vous sur le petit dossier à SANS INSERT, cliquez sur échap pour enregistrer']],
        'Insert': [
            (0, 0),
            [
                'Au niveau du rajout de modele de DT placez-vous sur le petit dossier à INSERT, cliquez sur échap pour enregistrer']],
        'Operation': [
            (0, 0),
            [
                'Basculez au bas de la page et placez-vous sur l\'opération info génerales, cliquez sur échap pour enregistrer']],
        'Operation modif': [
            (0, 0),
            [
                'Cliquez sur l\'operation info générales et placez-vous sur modifier l\'operation, cliquez sur échap pour enregistrer']],
        'Operation sans ins': [
            (0, 0),
            [
                'Supprimez une opération, basculez au bas de la page et placez-vous sur l\'opération info génerales, cliquez sur échap pour enregistrer']],
        'Operation sans ins modif': [
            (0, 0),
            [
                'Après avoir supprimé une opération, cliquez sur l\'operation info générales et placez-vous sur modifier l\'operation, cliquez sur échap pour enregistrer']],
        'Commentaire': [
            (0, 0),
            [
                'Ouvrez une opération, basculez au bas et placez-vous sur l\'espace de commentaire, cliquez sur échap pour enregistrer']],
        'Espace Valider': [
            (0, 0),
            [
                'Ouvrez une opération, basculez au bas et placez-vous sur l\'espace à gauche du bouton valider, cliquez sur échap pour enregistrer']],
        'Fermer': [
            (0, 0),
            [
                'Basculez au bas de la page et placez-vous sur le bouton fermer, cliquez sur échap pour enregistrer']] }