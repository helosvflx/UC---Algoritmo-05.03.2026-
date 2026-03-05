import random
numeros = [91, 34, 67, 15, 82]
print("Lista original: ", numeros)

numeros.sort()
print("Após sort(): ", numeros)

numeros.sort(reverse=True)
print("Após sort(): ", numeros)


numeros3 = [6, 7, 8, 9, 10]
random.shuffle(numeros3)
print("Lista embaralhadas: ", numeros3)

#desafio

numeros4 = [5, 19, 20, 50, 20, 40]
numeros4.sort()
print("Após sort(): ", numeros4)

numeros4.sort(reverse=True)
print("Após sort(): ", numeros4)

random.shuffle(numeros4)
print("Lista embaralhadas: ", numeros4)