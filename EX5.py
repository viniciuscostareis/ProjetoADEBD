numeros_inteiros=[]
for i in range(2):
  numeros_int=int(input("Digite um numero inteiro "))
  numeros_inteiros.append(numeros_int)

soma= sum(numeros_inteiros)
print(soma)

subtracao=numeros_inteiros[0]-numeros_inteiros[1]
print(subtracao)

multiplicacao=numeros_inteiros[0]*numeros_inteiros[1]
print(multiplicacao)

potencia=numeros_inteiros[0]**numeros_inteiros[1]
print(potencia)

def soma(a, b):
    return a + b

def subtracao(a, b):
    resultado = a
    if b < 0:
        b = -b
        for _ in range(b):
            resultado = soma(resultado, 1)
    else:
        for _ in range(b):
            resultado = soma(resultado, -1)
    return resultado

def multiplicacao(a, b):
    resultado = 0
    positivo = True
    if b < 0:
        b = -b
        positivo = False
    if a < 0:
        a = -a
        positivo = not positivo
    for _ in range(b):
        resultado = soma(resultado, a)
    return resultado if positivo else -resultado

def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado = multiplicacao(resultado, a)
    return resultado


numeros_inteiros = []
for i in range(2):
    numero = int(input(f"Digite o número inteiro {i+1}: "))
    numeros_inteiros.append(numero)

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potência")

opcao = int(input("Digite o número da operação desejada: "))

a = numeros_inteiros[0]
b = numeros_inteiros[1]

# Executar a operação
if opcao == 1:
    print(f"Resultado: {soma(a, b)}")
elif opcao == 2:
    print(f"Resultado: {subtracao(a, b)}")
elif opcao == 3:
    print(f"Resultado: {multiplicacao(a, b)}")
elif opcao == 4:
    print(f"Resultado: {potencia(a, b)}")
else:
    print("Opção inválida!")