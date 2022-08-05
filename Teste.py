#Pergunta ao cliente

print("Olá, vou lhe fazer uma pergunta")

#Sistema wile de repetição
while True :
    
    #menu com pergunta 
    resposta = input ('''
    Como você está?

    [Bem]

    [Mal]

    ''')



    #if (Se) a resposta for bem, mostrrar "que bom continue assim"
    if resposta == "bem" or resposta == "Bem" or resposta == "ótimo" or resposta == "ok":
    
        print ("Que bom, continue assim")
        break

    #Elif faz parte da lógica do if, como se fosse um "Se não" dentro do if.
    elif resposta == "mal" or resposta == "Mal" or respoosta == "Ruim" or resposta == "ruim":
        
        print ("Não desanime!")
        break

        #Break é a finalização do WHILE TRUE

    else: print ("Responda com bem ou mal")
    #O else fará com que qualquer coisa respondida sem ser "bem" ou "mal"voltará a mesma pergunta.



#                _                       
#                \`*-.                   
#                 )  _`-.                
#                .  : `. .               
#                : _   '  \              
#               ; *` _.   `*-._         
#               `-.-'          `-.      
#                  ;       `       `.    
#                  :.       .        \   
#                  . \  .   :   .-'   .  
#                  '  `+.;  ;  '      :  
#                  :  '  |    ;       ;-.
#                  ; '   : :`-:     _.`* ;
#         [bug] .*' /  .*' ; .*`- +'  `*'
#               `*-*   `*-*  `*-*'                                         
