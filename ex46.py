#Desenvolva um codigo python que leia 3 notas 
# calcule a media, se a media for maior ou igual a 6
#imprima aprovado, senao imprima recuperaçao
#identaçao
n1= float (input("Digite a primeira nota=>"))
n2= float (input("Digite a segunda nota=>"))
n3= float (input("Digite a terceira nota=>"))
media= (n1+n2+n3) / 3 
print (f"Media final: {media}")
if media>= 6:
    print ("Aprovado")
else:
    print ("Recuperação")    