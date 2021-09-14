import numpy as np

def crie_matriz(nLinhas, nColunas, valor):
    matriz = [] # lista vazia
    j = 0
    for i in range(nLinhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(nColunas):
            linha.append(valor[j])
        # coloque linha na matriz
        matriz.append(linha)
    return matriz

#lendo arquivo
file = open("instance1.txt","r")

instancia = []

for line in file:
    instancia.append(line.rstrip())
    
#Numero de Variaveis
nVar = int(instancia[0].split()[0])
print("Numero de variaveis: "+ str(nVar))

#Numero de Restrições
nRes = int(instancia[0].split()[1])
print("Numero de restricoes: " + str(nRes))

#Os coeficientes
coeficientes = [] 
for coef in range(0,nVar):
    coeficientes.append(int(instancia[1].split()[coef]))
print("Coeficientes: "+ str(coeficientes))

#As restrições
trestricoes = instancia[2:]
restricoes = []

#b = instancia[2:][nVar]
#print('B É: ' + str(b))

for i in trestricoes:
    restricoes.append((i.split()))
i = -1
t = len(restricoes)
while i < t-1:
    i=i+1
    j=0
    while j < (nVar+1):
        restricoes[i][j] = int(restricoes[i][j])
        j=j+1
print("Restricoes: ", restricoes)

i = 0
b = []
while i <= t-1:
    b.append(restricoes[i][nVar])
    i+=1

print("B É: " + str(b))

print(instancia)

# Colocando na forma padrão

nVar = nVar + nRes

i = 0

while i < nRes:
    coeficientes.append(0)
    i+=1

# Transpondo a matriz dos coeficientes

coeficientes = crie_matriz(1,nVar,coeficientes)

coeficientes = np.transpose(coeficientes)

print("Coeficientes: "+ str(coeficientes))

# Transpondo b

b = crie_matriz(1, nRes, b)

b = np.transpose(b)

print("B TRANSPOSTO: " + str(b))

# Criando A

# i = 0
# j = 0
# k = 0
# a = []
# while i <= nRes:
#     while k < nVar - 1:
#         if k < nVar - nRes:        
#             a.append(restricoes[i][k])
            
#         else:
#             for j in range(nRes):
#                 if j == i:
#                     a[i][k] = "-1"
#                 else:
#                     a[i][k] = "0"
#         k += 1
#     i+=1

a = restricoes
i=0
for i in range(len(a)):
    #print("ASDJHASKJDH" + str(a))
    a[i].pop()

    for j in range(nRes):
        if j == i:
            a[i].append(-1)
        else:
            a[i].append(0)
print(str(a))

# A = crie_matriz(nRes, nVar, a)
# print("A É:" + str(A))