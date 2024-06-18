def corrDyslexie(texte):
    correction = texte.replace("ua", "au")
    print(f"Voici votre texte corrigé : \n{correction}")

texte = input("Entrer votre texte: ")
corrDyslexie(texte)