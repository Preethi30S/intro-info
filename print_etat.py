# Implementer une fonction qui prend en argument l'etat du jeu, et affiche le jeu. Cette fonction ne retourne rien.

"""
1e representation : 4
2e representation : "---1------"
3e representation : [False, False, False, True, False, False, False, False, False, False, ]
"""

def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

state = [False, False, False, True, False, False, False, False, False, False, ]
print_state(repr3=state)

other_state = [True, False, False, False, False, False, False, False, False, False, ]
print_state(repr3=other_state)
