
def mon_nom_de_fonction(mon_parametre):
    ma_variable = mon_parametre + 2
    ma_variable_2 = ma_variable / 5
    #return ma_variable_2
    return None

print(2+2)

mon_resultat = mon_nom_de_fonction(1)
mon_resultat = mon_nom_de_fonction(2)

#####

ma_liste = ['Jules', 'Marie', 'Paul']
for mon_prenom in ma_liste:
    ma_variable = 'Bonjour ' + mon_prenom

    print(ma_variable)

print(2+2)

#####

compteur = 0
while(compteur < 10):
    print(compteur)
    compteur = compteur + 1

#while(True):
#    pass


######

"Le personnage est dans la salle 8."

position_personnage = 7

etat_des_salles = [False, False, False, False, False, False, False, True, False, False, ]

affichage_jeu = '-------X--'

######

"Le personnage est dans la 3e colonne, la 6e ligne"

position_personnage = (2, 5)

etat_des_salles = [
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, True, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
    [False, False, False, False, False, False, False, False, ],
]

etat_des_salles_dict = {
    'ligne0': [False, False, False, False, False, False, False, False, ],
    'ligne1': [False, False, False, False, False, False, False, False, ],
    'ligne2': [False, False, False, False, False, False, False, False, ],
    'ligne3': [False, False, False, False, False, False, False, False, ],
    'ligne4': [False, False, False, False, False, False, False, False, ],
    'ligne5': [False, False, True, False, False, False, False, False, ],
    'ligne6': [False, False, False, False, False, False, False, False, ],
    'ligne7': [False, False, False, False, False, False, False, False, ],
    'ligne8': [False, False, False, False, False, False, False, False, ],
    'ligne9': [False, False, False, False, False, False, False, False, ],
}

affichage_jeu = """----------
----------
----------
----------
----------
--+-------
----------
----------
----------
----------"""

print(affichage_jeu)


