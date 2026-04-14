# Desenvolva um codigo python em que o usuario 
#digite um numero e ira mostrar a tabuada deste 
#numero usando while 
n= int(input("Digite um valor=>"))
i= 0
while i <= 10:
    resultado= n*i
    print(f"{n}* {i}= {resultado}")
    i+= 1