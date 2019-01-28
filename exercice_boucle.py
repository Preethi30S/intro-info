"""
Solution 1: trop longue

print(0)
print(2)
print(4)
print(6)
print(8)
print(10)
print(12)
print(14)
print(16)
print(18)
print(20)
print(22)
print(24)
print(26)
print(28)
print(30)
"""

# Solution 2
# Inconvenient : facile de faire une erreur
"""
nombres = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

for nombre in nombres:
    print(nombre)
"""

# Solution 3
# Inconvenient : repose sur une astuce
"""
for nombre in range(16):
    print(nombre * 2)
"""

# Solution 4

for nombre in range(0, 31, 2):
    print(nombre)
