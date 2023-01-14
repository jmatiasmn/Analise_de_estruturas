import math

# Insira os dados abaixo, para valores com casas decimais separe com o ponto e para um novo valor separe com vírgula
n = int(input('Digite a quantidade de trechos  da barra: ')) #Aqui será perguntada o numero de trechos da barra
t = [] #Aqui será adicionado o torque de cada seção
d = [] #Aqui será adicionada a qual distância do ponto x = 0 o torque da seção está aplicado
c = [] #Aqui será adicionado o raio da seção
L = [] #Aqui será adicionado o tamanho da seção

#Adicionando valores
for trecho in range(1,n+1):
    torque = float(input('Digite o torque na seção {} em N.m: '.format(trecho)))
    t.append(torque)
    distancia = float(input('Digite a distância de aplicação do torque T{} seção {} em m: '.format(trecho,trecho)))
    d.append(distancia)
    raio = float(input('Digite o raio da seção {} em m: '.format(trecho, trecho)))
    c.append(raio)
    comprimento = float(input('Digite o comprimento da seção {} em m: '.format(trecho, trecho)))
    L.append(comprimento)
while True:
   x = float(input('Ponto em que você deseja calcular : '))
   if x > round(sum(L),2) :
      print('===A distancia x digitada é maior que o valor do comprimento total da peça, digite um valor válido===')
      
   elif x <0:
      print('Valores negativos são inválidos')
      
   else:
      break
      
#Calculo do torque no ponto X
torque_dist_x = 0
for secao in range(len(d)):
     if d[secao] <= x :
        torque_secao = t[secao]
        torque_dist_x += torque_secao
     elif x < d[0]:
        raio = c[0]
        torque_secao = 0
        torque_dist_x += torque_secao
        J = math.pi * math.pow(raio, 4) / 2
        cisalhamento_maximo = raio * torque_dist_x / J
        break
        
#Acha o raio no ponto x e calcula o cisalhamento no ponto
i = 0
aux = 0
for indice in range(len(L)):
    soma = round(L[0]+aux,2)
    if 0 <= x <= soma:
        raio=c[i]
        J = math.pi * math.pow(raio,4) / 2
        cisalhamento_maximo = raio * torque_dist_x / J
        break
    else:
        aux += L[i + 1]
        i+=1

print('----------------------------Resultados----------------------------')
print('O torque resultante atuante na seção de distância x={} m é {} N.m'.format(x,torque_dist_x))
print('O raio na seção de distância x = {} m é {} m'.format(x, raio))
print('O momento de inércia polar na seção de distância x={} m é {:} mm^4'.format(x,J))
print('A tensão de cisalhamento máxima na posição x = {} m é {:.2f} MPa'.format(x,cisalhamento_maximo/1000000))

#encerrar
encerrar = int(input())
