#Desenvolva um codigo que o usuario digite 
# o peso e a altura e calcule o imc
# pesquise a formula do imc e ao final mostre o imc
p= float(input("Digite o seu peso=>"))
a= float(input("Digite sua altura=>"))
imc= p / (a * a)
print (f"Meu imc é {imc}")