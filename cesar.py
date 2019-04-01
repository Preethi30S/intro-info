
# La fonction index()

"""
ma_liste = ['Arthur', 'Gérard', 'Alexandra']

mon_index = ma_liste.index('Arthur')
print(mon_index)
"""
# 

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


mon_index = alphabet.index('E')
print(mon_index + 3)

nouvelle_lettre = alphabet[mon_index + 3]

print(nouvelle_lettre)




def chiffrer(texte_a_chiffrer, decalage):
    if decalage > 25:
        print('Erreur ! Decalage trop important')
        return


    texte_chiffre = ''
    for lettre in texte_a_chiffrer:
        if lettre == ' ':
            nouvelle_lettre = ' '
        else:

            mon_index = alphabet.index(lettre)
            nouvel_index = mon_index + decalage

            if nouvel_index >= 26:
                nouvel_index = nouvel_index - 26

            nouvelle_lettre = alphabet[nouvel_index]
        texte_chiffre = texte_chiffre + nouvelle_lettre
    print(texte_chiffre)

#chiffrer(texte_a_chiffrer="BONJOUR MONDE", decalage=3)
#chiffrer(texte_a_chiffrer="BONJOUR CA VA", decalage=3)
#chiffrer(texte_a_chiffrer="REBONJOUR", decalage=4)
#chiffrer(texte_a_chiffrer="REBONJOUR", decalage=42)
chiffrer(texte_a_chiffrer="BONNE NUIT ZZZ", decalage=1)
