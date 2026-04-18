import pandas as pd
df = pd.read_csv("ClassicDisco.csv")

#print(df.to_string()) #imprimi todos os dados da planilha
#exibe as 5 primeiras linhas
#print(df.head())
#exibe as 5 ultimas linhas
#print(df.tail(10))
#print(df[10:15]) #da linha 10 a 14
print(df.shape)
#numero de linhas e colunas
