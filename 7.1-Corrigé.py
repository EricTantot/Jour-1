ch = input("Entrer une chaîne de caractères: ")
i = 0
result = ""
while i < len(ch):
    if ch[i-1] != ch[i] :
        result = result + ch[i]
    i = i + 1
print(result)
