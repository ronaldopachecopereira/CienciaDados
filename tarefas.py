#x=10
#while x >= 0:
#    print(x)
#    x = x-1
#print("fogo") # print deve ficar no começo, "sair" do while

#########################

#time=input('informe o nome do time: ')
#if time=='flamengo':
 #   print('é um time carioca')
#elif time=='gremio':
#    print('é um time gaucho')
#elif time=='inter':
#    print('é um time gaucho também')
#else:
#    print('não temos informações suficientes')
    
    
#######################################

#numero=1
#quantidade=0
#soma=0

#while numero!=0:
#   numero=int(input('informe um numero: '))
#    if numero != 0:
#               soma+=numero
#               quantidade+=1
#print ("a quantidade é: ", quantidade)
#print ("a média é : ", soma/quantidade)

               
#############
#soma=0
#while True:
#    valor=int(input("digite um numero pra somar ou 0 pra sair" ))
#    if valor==0:
 #       break
 #   soma=soma+valor
#print(soma)    



####
#print("Ronaldo Pacheco Pereira")
#a=2
#b=5
#print((5*a)*(3*b))
 #######
#a=2
#b=5
#c=5
#print(a+b+c)

#######
 
#num1=int(input( "Digite o numero 1 "))
#num2=int(input("Digite o segundo numero "))
#operacao=input("Qual operação escolhida? Multiplicação (m), divisão (d), subtração (s), adção (a) ")
#if operacao=='m':
#    resultado=(num1*num2)
#elif operacao=='d':
#    resultado=(num1/num2)
#elif operacao=='s':
 #   resultado=(num1-num2)
#elif operacao=='a':
#    resultado=(num1+num2)
#print("O resultado da operação foi: ", resultado)


############################


#for x in range(1,11):
#    print(x)


##########################

#x=0
#while x<=10:
#    print(x)
#    x+=1

######################
#soma=0
#x=0
#for x in range(0,11):
#    if x %2==1:
#        print(x)
#    soma=soma+x
 #  
#print(" a soma deu: " , soma)

##################

##nome=str(input("Digite seu nome: "))
#sobrenome=str(input("Digite seu sobrenome: "))
#idade=int(input("digite sua idade: "))
#telefone=input("Digite seu telefone: ")
#cidade=str(input("Digite sua cidade: "))
#print( nome, sobrenome)
#print("(11)", telefone)
#print("idade: ", idade)
#print("Cidade: ", cidade)



#####################

#x=int(input("valor de x "))
#y=int(input("valor de y "))
#z=(x**2 + y**2)/ (x-y)**2
#print(z)

## ###
#L=[5,7,2,9,4,1,3]
#print(len(L))
#print(max(L))
#print(min(L))
#print(sum(L))
#print(L.sort())
#print(L.reverse())

#########
#L=list(range(1,51,3)) # isso cria uma lista com os multiplos de 3 entre 1 e 50
#print(L)
#######


#dicionario1={'arroz': 5.40, 'feijao':7.90, 'alface':9.90}

#print(dicionario1)
#print(dicionario1['feijao'])#para saber o valor da chave feijao
#dicionario1['carne']=29.90#adicionando mais itens ao dicionario
#dicionario1['tomate']=8.90
#print(dicionario1)
#if 'feijao' in dicionario1: #verificando se tem a chave feijao no dicionario
#    print("tem o item")
#soma = (sum(dicionario1.values()))#isso soma os valores dentro do dicionario
#itens = (len(dicionario1))#isso dá a contagem de chaves dentro do dicionario
#media=soma/itens
#print("a média de valores é de : ", media)


#############

#Nota1=int(input("digite a primeira nota: "))
#Nota2=int(input("digite a segunda nota: "))
#media=(Nota1+Nota2)/2
#if media < 6:
#    print("voce foi reprovado")
#else:
#    print("Voce foi aprovado")

###############

#Nota1=int(input("digite a primeira nota: "))
#Nota2=int(input("digite a segunda nota: "))
#media=(Nota1+Nota2)/2
#if media > 6:
#   print("voce foi aprovado")
#elif media >4:
#    print("Exame final")
#elif media <4:
 #   print("Voce foi reprovado")

 ###############
#soma=0
#x=0
#for x in range(1,334):
##    if x %3==0:
#        print(x)
 #   soma=soma+x
#   
#print(" a soma deu: " , soma)


###### exercicio 1
#print("Ronaldo Pacheco pereira")

########### exercicio 2
#a=2
#b=5
#print("o resultado é: ", (5*a)*(3*b))

####### exercicio 3
#a=2
#b=5
#c=5
#print("a soma é = ", a+b+c)

########## exercicio 4
#num1=int(input( "Digite o numero 1 "))
#num2=int(input("Digite o segundo numero "))
#operacao=input("Qual operação escolhida? Multiplicação (m), divisão (d), subtração (s), adção (a) ")
#if operacao=='m':
#    resultado=(num1*num2)
#elif operacao=='d':
#    resultado=(num1/num2)
#elif operacao=='s':
 #   resultado=(num1-num2)
#elif operacao=='a':
#    resultado=(num1+num2)
#print("O resultado da operação foi: ", resultado)


######### exercicio 5 a

#x=1
#while x <= 10:
#    print(x)
#    x = x+1


######### exercicio 5 b

#for x in range(1,11):
#    print(x)

###### exercicio 6 a

#soma=0
#x=0
#for x in range(1,11):
#    if x %2==1:
#        print(x)
#        soma=soma+x  
#print(" a soma deu: " , soma)

#################Exercicio 6 b
#soma=0
#x=0
#for x in range(1,11):
#    if x %2==0:
#        print(x)
 #       soma=soma+x  
#print(" a soma deu: " , soma)
 ######### exercicio 6 com while
#x=1
#soma=0
#while x <= 10:
#    x = x+1
#    if x %2==0:
 #       print(x)
 #       soma=soma+x
#print(" a soma deu: " , soma)
############## exercicio 6 com while
#x=1
#soma=0
#while x <= 10:
#    x = x+1
#    if x %2==1:
#        print(x)
#        soma=soma+x
#print(" a soma deu: " , soma)

######################### exercicio após bhaskara

# def, if, else, return
# def define a regra, if, else e return são condicionais

###########

#s="mentorama"
#print(s.upper())

############

#for vogal in "mentorama":
#   if vogal == "e":
#        continue
#    if vogal == "o":
#        continue
#    if vogal == "a":
#        continue

#    print(vogal)
    
##################

##nome=str(input("Digite seu nome: "))
#sobrenome=str(input("Digite seu sobrenome: "))
#idade=int(input("digite sua idade: "))
#telefone=input("Digite seu telefone: ")
#cidade=str(input("Digite sua cidade: "))
#print( nome, sobrenome)
#print("(11)", telefone)
#print("idade: ", idade)
#print("Cidade: ", cidade)

############# Bhaskara
#a = 1
#b = -5
#c = 6

#delta = (b ** 2) - 4 * a * c
#x1 = (-b + delta ** (1 / 2)) / (2 * a)
#x2 = (-b - delta ** (1 / 2)) / (2 * a)

#print("x1: {}, x2: {}".format(x1, x2))

################## bhaskara import math

import math

print("EQUACAO DE SEGUNDO GRAU")
print("ax^2 + bx + c = 0")

a = 1
b = -5
c = 6


delta = (b**2) - (4*a*c)
print("delta é", delta)


if (delta < 0):
    print("esta equação não possui raízes reais")
else:
    if (delta == 0):
        x = (-b) / (2*a)
        print("a raiz desta equação é", x)
    else:
        x_pos = ((-b) + math.sqrt(delta)) / (2*a)
        x_neg = ((-b) - math.sqrt(delta)) / (2*a)
        if (x_pos <= x_neg):
            print("as raízes da equação são", x_pos, "e", x_neg)
        else:
            print("as raízes da equação são", x_neg, "e", x_pos)
        
#print("FIM!!...")

    


    
    



 

















    
    







               


















