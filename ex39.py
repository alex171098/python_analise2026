#dESENVOLVA UM CODIGO PYTHON QUE ENVIE um valor
# para uma funçao que essa verifique se o numero
#  é impar ou par 
def par(a):
    if a % 2 == 0: 
        return "par"   
    else:
        return "impar"
v= int(input("Digite um valor"))
y= par(v)     
print (y)  
  


