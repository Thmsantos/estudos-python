# -*- coding: utf-8 -*-
"""exerc2.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/18k7XmeGy4H23nDifxAqs851DZ-WXyUzg
"""
#exerc_2
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

def main():
    
  matriz = gerarMatriz()

  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      
      elemento = matriz[i][j]
      
      print('o elemento: ', elemento, 'está na linha', i,'e na coluna', j)

main()
