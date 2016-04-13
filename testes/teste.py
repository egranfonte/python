'''
print "Calculadora"
num1 = raw_input('Digite um num1: ')
num2 = raw_input('Digite um num2: ')
simbolo = raw_input('qual comando? soma (+),subtracao(-)')

if simbolo == '+':
    total = float(num1) + float(num2)
else:
    total = float(num1) - float(num2)

print total
'''
#teste 2
'''
from datetime import datetime
print ('Bem-vindo ao Tradutor de Pig Latin!')
print (datetime.now())
# Comece seu codigo aqui!
original = input('Enter a word:')    
if len(original) > 0 and original.isalpha():
    print (original)
else:
    print ("Valor inválido, \nEstá em branco? Com numeros? \nFavor somente letras.")
'''

#teste 3
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (original)
    print(new_word)
else:
    print (empty)