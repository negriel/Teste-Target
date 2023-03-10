string = input("Digite a string a ser invertida:")
invertido = ""

for i in range(len(string)):
    index = (len(string)-1)-i
    invertido += string[index]

print(f"A string invertida e: {invertido}")