class CoordonnéesExcel:

    def __init__(self, fichier, feuille, celulle1, celulle2):
        self.feuille = feuille
        self.celulle1 = celulle1
        self.celulle2 = celulle2
        self.fichier = fichier
        self.ws = fichier.Sheets(feuille)
        self.liste = []
        self.itération = -1
        i = 2
        while self.ws.Range(self.celulle1 + str(i)).Value != None:
            self.liste.append([
                self.ws.Range(self.celulle1 + str(i)).Value,
                self.ws.Range(self.celulle2 + str(i)).Value])
            i += 1


    def get_coordonnées(self):
        self.itération += 1
        try:
            c = self.liste[self.itération]
        except:
            print('Erreur: Le nombre maxi de  coordonnées est atteint')
            c = False
        finally:
            return c




    def get_tout(self):
        return self.liste



class CoordonnéesEcran:
    profile = [
        'Khalil']
    dictio = {
        'Espace ajouter': [
            (0, 0),
            [
                'Dans l\'activité: gérer les données techniques placez-vous sur: l espace blanc à droite du boutton ajouter, cliquez sur échape pour enregistrer']],
        'Dossier': [
            (0, 0),
            [
                'Basculer au bas de la page et placez-vous sur le dossier, cliquez sur échape pour enregister']],
        'Composant': [
            (0, 0),
            [
                'Basculer au bas de la page et Cliquez sur le dossier et placez-vous sur: ajouter un composant, cliquez sur échape pour enregister']],
        'Dossier2': [
            (0, 0),
            [
                'Apres le rajout de composant basculer au bas de la page et placez-vous sur le dossier, cliquez sur échape pour enregister']],
        'ChoixDt': [
            (0, 0),
            [
                'Basculer au bas de la page et Cliquez sur le dossier et placez-vous sur: importer des DT, cliquez sur échape pour enregister']],
        'Sans Insert': [
            (0, 0),
            [
                'Au niveau du rajout de modele de DT placez-vous sur le petit dossier à SANS INSERT, cliquez sur échape pour enregister']],
        'Insert': [
            (0, 0),
            [
                'Au niveau du rajout de modele de DT placez-vous sur le petit dossier à INSERT, cliquez sur échape pour enregister']],
        'Operation': [
            (0, 0),
            [
                'Basculez au bas de la page et placez-vous sur l opération info génerales, cliquez sur échape pour enregister']],
        'Operation modif': [
            (0, 0),
            [
                'Cliquer sur l operation info generales et placez-vous sur modifier l operation, cliquez sur échape pour enregister']],
        'Operation sans ins': [
            (0, 0),
            [
                'Supprimer une operation, basculez au bas de la page et placez-vous sur l opération info génerales, cliquez sur échape pour enregister']],
        'Operation sans ins modif': [
            (0, 0),
            [
                'Après avoir supprimé un opération, liquer sur l operation info generales et placez-vous sur modifier l operation, cliquez sur échape pour enregister']],
        'Commentaire': [
            (0, 0),
            [
                'Ouvrez une opération, basculez au bas et placez-vous sur l espace de commentaire, cliquez sur échape pour enregister']],
        'Espace Valider': [
            (0, 0),
            [
                'Ouvrez une opération, basculez au bas et placez-vous sur l espace à gauche du button valider, cliquez sur échape pour enregister']],
        'Fermer': [
            (0, 0),
            [
                'Basculez au bas de la page et placez-vous sur le boutton fermer, cliquez sur échape pour enregister']] }