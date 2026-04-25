#Desenvolva  um codigo python que leia o salario
# de um funcionario se o salario for maior que 5000
#calucle o irrf que sera 7,5% sobre o salario
#se for maior que 5000 nao paga imposto Ir 
# e se for maior que 8000 o imposto será 
#27% ao final mostre o salario
# o valor do imposto pago e o slario final
s= float(input("Digite o salario=>"))
if s<= 5000:
    imposto= 0
elif s<= 8000:
    imposto= s *  0.075
else:
    imposto=s * 0.27 
sal_final= s - imposto 
print(f"Salario  {s}, imposto  {imposto}, salario bruto {sal_final}")          