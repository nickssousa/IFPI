def displayMenu(): 
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:") 
    print(" c = converter uma frase")
    print(" p = imprimir dicionário")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")
    
#----- 
def convertSentence(): 
    sentence = input("Insira uma frase para traduzir: ").lower() 
    translatedSentence = ""
    listofwords= sentence.split()

#divide a frase em uma lista de palavras listofwords = sentence.split() 
    for word in listofwords: 

#adiciona a palavra traduzida se ela existir no dicionário 
        if word in textspeakDictionary: 
            translatedSentence += textspeakDictionary[word] + " "
            
#mantém a palavra original caso não exista tradução
        else: 
            translatedSentence += word + " " 

#imprime a frase traduzida
            print("==>")
            print(translatedSentence) 

#----------------------------------------------------------
def addDictionaryItem():
    textToAdd= input("Insira a expressão a ser adicionada ao dicionário; ")
    meaning= input("O que ela significa?: ")
    if textToAdd in textspeakDictionary:
        print("Essa palavra já está no dicionário")
    else:
        textspeakDictionary[txtToAdd] = meaning

def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida do dicionário: ")
    if txtToDelete in textspeakDictionary:
        del textspeakDictionary[txtToDelete]
    else:
        print("Essa palavra não existe")

textspeakDictionary = {
    "rs" : "risos",
    "tmb" : "também",
    "vc" : "você",
    "pq" : "por que"
 }

running = True

displayMenu()

while running == True:
    menuChoice = input(">_").lower()

    if menuChoice == 'c':
        convertSentence()

    elif menuChoice == 'p':
        print(textspeakDictionary)

    elif menuChoice == 'a':
        addDictionaryItem()

    elif  menuChoice == 'd':
        deleteDictionaryItem()

    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")
