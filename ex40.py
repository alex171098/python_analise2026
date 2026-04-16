#Crie uma funcao que receba o lado de um quadrado 
# e retorne o valor de sua area (A = lado ^2)
#a = l ** 2
def quadrado(lado):
     return lado ** 2
medida_lado = float (input("Digite a medida de um lado do quadrado"))
area = quadrado (medida_lado)
print (f"A área do quadrado é:{area}")