"""
Définir une fonction qui prend en paramètre une liste et qui retourne son 5e élément. Tester cette fonction sur plusieurs listes. Que se passe-t-il si la liste est trop courte ?
"""

def item_getter_5(ma_liste):
    return ma_liste[4]

exemple_liste = ['a', 'b', 'c', 'd', 'e', 'f']
if item_getter_5(exemple_liste) == 'e':
    print("test OK")
else:
    print("test KO")

mauvaise_liste = ['a', 'b', 'c']
item_getter_5(mauvaise_liste)