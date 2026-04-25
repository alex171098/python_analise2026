#Desenvolva um programa que seja capaz de coletar 
# uma sequencia de 5 numeros inteiros fornecidos 
#pelo usuario ao final da leitura desses valores,
#o programa devecalcular o somatorio total e exibir o resultado na tela 
soma= 0 
for i in range (0, 5):
    n= int(input("Digite um numero=>"))
    soma = soma + n 
print (f"O somatorio de todas as notas é {soma}")    
