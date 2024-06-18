s = input("Entrer une chaîne de caractères: ")

long = len(s)
print(f"Cette Chaîne de caractères fait {long} caractères.")

space = s.count(" ")
print(f"Cette Chaîne de caractères a {space} espaces.")

new = s.replace(" ", "")
print(f"Chaîne de caractères sans les espaces : '{new}'")


