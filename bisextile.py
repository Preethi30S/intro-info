"""
Implémenter une fonction qui prend en argument une année, et retourne True si l'année est bisextile. 
"""
"""
def is_bisextile(year):
    # multiple de 4
    if year % 4 == 0:

        # multiple de 100
        if year % 100 == 0:

            # multiple de 400
            if year % 400 == 0:
                return True

            return False

        return True
    else:
        pass
    return False
"""

"""
def is_bisextile(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
"""

def is_bisextile(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False



print(is_bisextile(2019)) # False
print(is_bisextile(2004)) # True
print(is_bisextile(1900)) # False : multiple de 100 mais pas de 400
print(is_bisextile(2000)) # True : multiple de 400
