"""
A l'aide de deux boucles, définir une liste qui contient 5 fois l'élément False, une fois l'élément True puis trois fois l'élément False. En quoi cela peut-il vous aider à passer de la représentation 1 à la représentation 3 ?
"""

def build_list(i):
    new_list = []

    for compteur in range(i):
        new_list.append(False)
    new_list.append(True)
    for compteur in range(8-i):
        new_list.append(False)

    return new_list

new_list = build_list(5)
if new_list == [False, False, False, False, False, True, False, False, False]:
    print("test OK")
else:
    print("test KO")
