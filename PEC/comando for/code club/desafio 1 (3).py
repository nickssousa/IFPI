textSpeakDictionary= {
    "rs" : "risos",
    "tbm" : "também",
    "vc" : "você",
    "pq" : "porque",
    "tmj" : "tamo junto",
    "s" : "sim",
    "n" : "não"
    }

#obtem a frase para tradução
sentence = input("Insira uma frase para traduzir:").lower()

#divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSentence = ""

for word in wordsToTranslate:
    #adiciona a palavra traduzia caso ela exista no dicionario
    if word in textSpeakDictionary:
        translatedSentence+= textSpeakDictionary[word]+ " "

        #mantem a palavra original caso nao exista tradução
    else:
        translatedSentence+= word+ " "

#imprime a frase traduzida
print("===>")
print(translatedSentence)
