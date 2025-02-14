# Missão 1

nota = int(input('Digite a nota do Aluno:'))

if nota >=6:
    print('O aluno foi aprovado!')
else:
    print('O aluno foi reprovado!')



# Missao 2

idade = int(input('Digite a sua idade para saber se poderá votar!'))

if idade >=16:
    print('Parabéns!Voce pode votar!')
else:
    print('Infelizmente voce nao pode votar ainda!')



# Missao 3

notap = float(input('Insira a nota da prova!'))

if notap >=90 and nota <=100:
    print('Parabéns, voce tirou A!')
elif notap >=80 and nota <=89:
    print('Muito bem, voce tirou B.')
elif notap >=70 and nota <=79:
    print('Bom trabalho, voce tirou C.')
elif notap >=60 and nota <=69:
    print('FIque atento, voce tirou D.')
else:
    print('Estude um pouco mais, voce tirou F.')


# Missao 4

valor1 = float(input('Insira o primeiro valor a ser somado!'))
valor2 = float(input('Insira o segundo valor a ser somado!'))

total = valor1 + valor2

print(f'O resultado final é de:{total}')


# Missao 5

senha_de_acesso = 'Python123'
senha_inserida = input('Digite sua senha:')

if senha_inserida == senha_de_acesso:
    print('Senha Correta, acesso permitido!')
else:
    print('Senha invalida, acesso negado!')


# Missao 6

verificacao = 1

while verificacao <= 10:
    print(f'Processando {verificacao} dados')
    verificacao += 1

# Missao 7

numeros = [8, 3, 10, 1, 5]
numeros.sort()

print(f'Organizando os numeros {numeros} de forma ordenada')



# Missao 8


alunos = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')

print(f'Primeiro nome da lista:{alunos[0]} e ultimo nome da lista:{alunos[4]}')



# Missao 9

def dobro():
    resultado = 5 * 2
    print (f"O dobro do numero informado é {resultado}")

dobro()



# Missao 10

nome = 'Ana'
quant_carac = len(nome)
print('O nome contem', quant_carac, 'caracteres')


