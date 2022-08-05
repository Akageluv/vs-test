#Pergunta ao cliente
print("Olá, vou lhe fazer uma pergunta")

#Sistema wile de repetição
while True :
    #Pergunta com variavél "Resposta"
    resposta = input ("como você está? ")
    #if (Se) a resposta for bem, mostrrar "que bom continue assim"
    if resposta == "bem":
    
        print ("Que bom, continue assim")
        break
    #Elif faz parte da lógica do if, como se fosse um "Se não" dentro do if.
    elif resposta == "mal":

        print ("Não desanime!")
        break

        #Break é a finalização do WHILE TRUE

    else: print ("Responda com bem ou mal")
    #O else fará com que qualquer coisa respondida sem ser "bem" ou "mal"voltará a mesma pergunta.
