# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WvEwhhlX02HMeIFN_6mLpQiCS0KEtpvC
"""

# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
# Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
#
# Entrada:
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.
#
# Saída:
# Imprima o nome do animal correspondente à entrada fornecida.
#
# Exemplos de Entrada        Exemplos de Saída
# vertebrado                 homem
# mamifero
# onivoro
#
# vertebrado                 aguia
# ave
# carnivoro
#
# invertebrado               minhoca
# anelideo
# onivoro

a = str(input())
b = str(input())
c = str(input())

if(a == 'vertebrado'):
  if(b == 'ave'):
    if(c == 'carnivoro'):
      print('aguia')
    elif(c == 'onivoro'):
      print('pomba')
  elif(b == 'mamifero'):
    if(c == 'onivoro'):
      print('homem')
    elif(c == 'herbivoro'):
      print('vaca')
elif(a == 'invertebrado'):
  if(b == 'inseto'):
    if(c == 'hematofago'):
      print('pulga')
    elif(c == 'herbivoro'):
      print('lagarta')
  elif(b == 'anelideo'):
    if(c == 'hematofago'):
      print('sanguessuga')
    elif(c == 'onivoro'):
      print('minhoca')