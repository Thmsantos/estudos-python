# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lRklYQnr44iVfSt5EW9vX4ACs4pc95D0
"""

#Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

#Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

#Entrada
#O arquivo de entrada contém um valor inteiro.

#Saída
#Imprima a saída conforme exemplo fornecido.

n = int(input())

ano = n / 365
n = n % 365

meses = n / 30
n = n % 30

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (int(ano), int(meses), int(n)))