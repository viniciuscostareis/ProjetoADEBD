alunos=[]
for i in range(10):
    nome = input("Digite seu nome: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append({"nome": nome, "nota": nota})

soma_notas = sum(aluno["nota"] for aluno in alunos)
media = soma_notas / len(alunos)
print(media)

soma_notas = sum(aluno["nota"] for aluno in alunos)
media = soma_notas / len(alunos)
print(media)

maior_nota = max(aluno["nota"] for aluno in alunos)
menor_nota = min(aluno["nota"] for aluno in alunos)

alunos_maior = [aluno["nome"] for aluno in alunos if aluno["nota"] == maior_nota]
alunos_menor = [aluno["nome"] for aluno in alunos if aluno["nota"] == menor_nota]

print(f"O(A) {', '.join(alunos_maior)} tirou a maior nota: {maior_nota}")
print(f"O(A) {', '.join(alunos_menor)} tirou a menor nota: {menor_nota}")

abaixo_media = [aluno for aluno in alunos if aluno["nota"]<media]
print("Alunos abaixo da média:")
for aluno in abaixo_media:
    print(f"{aluno['nome']} - Nota: {aluno['nota']}")