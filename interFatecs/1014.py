# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oz1lFrKmiMeEHXU54A9Zea-BmY-1oNAk
"""

#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

#Entrada
#O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando
#o total de combustível gasto, com um dígito após o ponto decimal.

#Saída
#Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

x = int(input())
y = float(input())

print("%0.3f km/l" % (x/y))