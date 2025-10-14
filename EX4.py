numeros_mega=[]
for i in range(6):
    mega = int(input("Digite um número: "))
    numeros_mega.append(mega)
numero_cartão=[]
for i in range(6):
    cartão = int(input("Digite um número: "))
    numero_cartão.append(cartão)
pontos = 0
for numero in numero_cartão:
    if numero in numeros_mega:
        pontos += 1

print(f"\nVocê acertou {pontos} número(s)!")