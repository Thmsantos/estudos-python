# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g851C9PNR0xih8OV-FuKLnNiHoZvB5vJ
"""

# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#
# Perimetro = XX.X
#
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:
#
# Area = XX.X
#
# Entrada:
# A entrada contém três valores reais.
#
# Saída:
# O resultado deve ser apresentado com uma casa decimal.
#
# Exemplo de Entrada    Exemplo de Saída
# 6.0 4.0 2.0          Area = 10.0
# 6.0 4.0 2.1          Perimetro = 12.1

a, b, c = map(float, input().split())

if(a < (b+c) and b < (c + c)):
  print("Perimetro = %.1f" % (a + b + c))
else:
  print("Area = %.1f" % (((a + b) * c) / 2))