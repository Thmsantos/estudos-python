# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16kNcqZXXbFlO3cWKhUUWhvmpTSdYTbQB
"""

# Leia 3 valores inteiros e ordene-os em ordem crescente.
# No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
# Entrada: A entrada contém três números inteiros.
# Saída: Imprima a saída conforme foi especificado.

# Exemplo de Entrada    Exemplo de Saída
# 7 21 -14

# -14
# 7
# 21

# 7
# 21
# -14

# -14 21 7

# -14
# 7
# 21

# -14
# 21
# 7

x = list(map(int, input().split()))[:3]
Inversa = sorted(x)

if(x[0] > x[1] and x[0] > x[2]):
  Inversa[2] = x[0]
  if(x[1] > x[2]):
    Inversa[0] = x[2]
    Inversa[1] = x[1]
  elif(x[1] < x[2]):
    Inversa[0] = x[1]
    Inversa[1] = x[2]
elif(x[0] > x[1] and x[0] < x[2]):
  Inversa[0] = x[1]
  Inversa[1] = x[0]
  Inversa[2] = x[2]
elif(x[0] < x[1] and x[0] > x[2]):
  Inversa[0] = x[2]
  Inversa[1] = x[0]
  Inversa[2] = x[1]

for i in Inversa:
  print(i)
print()
for j in x:
  print(j)