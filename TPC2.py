from collections import Counter
import collections
import sys

A = ["1P", "1C", "1O", "2P", "2C", "2O", "2E", "3P", "3C", "3O",
     "3E", "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", 
     "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", 
     "DC", "DO", "DE", "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", 
     "1P", "1C", "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", 
     "4P", "4C", "4O", "4E", "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", 
     "7O", "7E", "8P", "8C", "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", 
     "JP", "JC", "JO", "JE", "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE", "1P", "1C", 
     "1O", "1E", "2P", "2C", "2O", "2E", "3P", "3C", "3O", "3E", "4P", "4C", "4O", "4E", 
     "5P", "5C", "5O", "5E", "6P", "6C", "6O", "6E", "7P", "7C", "7O", "7E", "8P", "8C", 
     "8O", "8E", "9P", "9C", "9O", "9E", "DP", "DC", "DO", "DE", "JP", "JC", "JO", "JE", 
     "VP", "VC", "VO", "VE", "RP", "RC", "RO", "RE"]


    
for i in A:
    if (len(A)>=52 ):
        print("A lista tem",len(A),"cartas")
        break
    else:
        print("Não há cartas suficientes na lista para fazer um baralho completo")
        sys.exit()
        break


contagem = collections.Counter(A)
print("Contagem das cartas em comum no baralho: ",contagem)
print("A contagem da carta menos recorrente é:",contagem.most_common()[:-1-1:-1],"logo há",contagem.most_common()[:-1-1:-1],"baralho(s)")
