# -*- coding: utf-8 -*-
"""exerc_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1puif63Wb8-UIy_sA4xLwNMZkXRlJoMUs
"""

import random

def gerarMatriz():
  linha = random.randint(2, 5)
  coluna = random.randint(2, 5)

  matriz = []

  for i in range(linha):
    nova_linha = [0] * coluna

    for j in range(len(nova_linha)):
      nova_linha[j] = random.randint(1, 50)

    matriz.append(nova_linha)
  
  return(matriz)

numero = random.randint(1, 50)

def main(numero):
    
  matriz = gerarMatriz()

  numero = random.randint(1, 50)

  acumulador = 0

  for i in range(len(matriz)):
    acumulador = 0 
    for j in range(len(matriz[i])): 

      if (matriz[i][j] < numero):
        acumulador = acumulador + 1
    
    print(matriz[i], numero, acumulador)
    print('---------------------------')
      

main(numero)