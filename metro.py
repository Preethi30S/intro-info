"""
scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}

"BIBLIOTHEQUE"
"""


def calcul_score(mot):
    total = 0
    for lettre in mot:
        score_lettre = ord(lettre) - ord('A') + 1
        total = total + score_lettre

    print(total)

calcul_score(mot='BIBLIOTHEQUE')


#total = scores.get('B') + scores.get('I') + scores.get('B') + scores.get('L') + scores.get('I') + scores.get('O') + scores.get('T') + scores.get('H') + scores.get('E') + scores.get('Q') + scores.get('U') + scores.get('E')

#print(total)


scores.get('A')
scores['A']
