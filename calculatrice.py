nb1 = int(input("Entrer le premier chiffre: "))
nb2 = int(input("Entrer le second chiffre: "))
signe = input("Enter l'opérateur (+, -, *, /, %, //, **): ")

if signe == "+":
    result = nb1 + nb2 
    print(result)
elif signe == "-":
    result = nb1 - nb2
    print(result)
elif signe == "*":
    result = nb1 * nb2
    print(result)
elif signe == "/":
    result = nb1 / nb2
    print(result)
elif signe == "%":
    result = nb1 % nb2
    print(result)
elif signe == "//":
    result = nb1 // nb2
    print(result)
elif signe == "**":
    result = nb1 ** nb2
    print(result)
else:
    print("Veuillez entrer un opérateur présent dans les choix proposés.")
