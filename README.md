# Saisie-Auto

Fonctions ajoutées / Modifications effectuées :

 - Flexibilité avec le nombre de composants et d'opérations
    6 composants max
    20 opérations max
    L'ordre des composants n'est pas obligatoire mais ça peut faire gagner du temps

 - Composants dans les opérations indiquées 
    Mélange --> Extrusion
    Fournitures industrielles --> Moulage
    Autres --> Conditionnement
 
 - Détection si changements de pixels 
    fenêtre de rentrée du code article
    ajout d'une opération 
    ajout d'un composant

 - L'opération 'plateaux' devient un composant

 - Baisse du nombre de coordonées à configurer (avec calculs de pixels qui sont statiques peu importe l'écran)

 - Attente pour sélectionner l'article (code sylob non présent dans l'Excel, il peut y avoir plusieurs article pour un code devis) 

 - Meilleure ergonomie sur les valeurs récupérées de Excel

 - Bouton fermer sur le menu

 - Bouton informations sur le menu 

Informations de flexibilité : 

 - Suppression d'une donnée technique possible avant le lancement (écrit un message qui décale le bouton ajouter)

 - Recherche déjà en cours d'un article dans la fenêtre d'ajout pour la sélection de l'article prise en compte

 - Peut y avoir déjà des données techniques (Attention si le code est le même ça va sur la donnée technique existante)
