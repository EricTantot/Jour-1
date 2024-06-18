a = str(4) * int("3") # "444" : Oui
b = int("3") + float("3.2") # 6.2 : Oui
c = str(3) * float("3.2") # Erreur : Oui
d = str(3/4) * 2 # "3/43/4" : 0.750.75

print(a, b, d)