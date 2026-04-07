s= float(input("Digite o salário =>"))
if s<= 5000:
    imposto= 0 
elif s <= 8000:
    imposto= s*0.075
else:
    imposto= s*0.27
salfinal= s - imposto
print (f"Salário - {s}, imposto - {imposto}, Salário bruto {salfinal} ") 
print ("teste git")

