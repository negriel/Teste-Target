n = int(input("Digite um termo para saber se pertence a sequencia fibonacci: "))
ultimo=1
penultimo=1


if (n==0) or (n==1) or (n==2):
    print("pertence a sequencia")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    if(termo==n):
        print("pertence a sequencia")
    else:
        print("nao pertence a sequencia")
    
