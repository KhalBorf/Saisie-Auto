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

    def get_coordonnées(self):
        #print(self.liste[0])
        try:
            self.set_itération()
            c = self.liste[self.itération]
            
        except:
            print('Le nombre maximum de coordonnées est atteint')
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
            print('Le nombre maximum de coordonnées est atteint')
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
                'Dans l\'activité: gérer les données techniques, placez-vous sur le bouton AJOUTER sans cliquer dessus, cliquez sur échap pour enregistrer']],
        'Fenêtre ajouter': [
            (0, 0),
            [
                'Dans l\'activité: gérer les données techniques, cliquez sur le bouton AJOUTER puis sur la loupe avec un + à l\'intérieur, placez vous sur la bande de votre couleur SYLOB à droite de RECHERCHE SUR LES ARTICLES, soyez bien sur la bande de couleur, cliquez sur échap pour enregistrer, puis annulez']],
        'Dossier': [
            (0, 0),
            [
                'Allez dans une donnée technique complète en mode EDITION, basculez au bas de la page et placez-vous sur le texte juste à droite du dossier (il doit être souligné), cliquez sur échap pour enregistrer']],
        'Operation': [
            (0, 0),
            [
                'Basculez en haut de la page, cliquez sur le texte à droite du dossier et placez-vous sur AJOUTER UNE OPÉRATION, cliquez sur échap pour enregistrer']],
        'Fenetre Operation': [
            (0, 0),
            [
                'Cliquez sur AJOUTER UNE OPÉRATION et placez-vous sur le champ gris à droite de OPÉRATION MODELE, cliquez sur échap pour enregistrer, puis annulez']],
        'Commentaire Operation': [
            (0, 0),
            [
                'Ouvrez une opération, basculez au bas et placez-vous en bas à droite de la zone de texte de l\'espace de commentaire, cliquez sur échap pour enregistrer']],
        'Composant': [
            (0, 0),
            [
                'Basculez en haut de la page, cliquez sur la première opération, puis sur AJOUTER UNE OPÉRATION AU DESSUS, mettez une opération modèle quelconque, quittez, puis cliquez sur l\'opération que vous venez de créer, placez vous sur AJOUTER UN COMPOSANT, cliquez sur échap pour enregistrer, puis supprimez l\'opération que vous venez de créer']],
        'Fenetre Composant': [
            (0, 0),
            [
                'Cliquez sur AJOUTER UN COMPOSANT et placez-vous sur le champ gris à droite de ARTICLE, cliquez sur échap pour enregistrer, puis annulez']]}