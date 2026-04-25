#Desenvolva um codigo python que entre com a idade e o genero 
#(m ou f )
#se a idade for maior igual a 18 eo genero m 
# imprima apto ao alistamento militar senao 
#imprima nao apto ao alistamento militar 
idade= int(input("Digite sua idade=>"))
genero= input("Digite M para masculino e F para femenino=>")
if idade>= 18 and genero== "M":
    print("Apto ao alistamento militar ")
else:
    print("Não apto ao alistamento militar")    
