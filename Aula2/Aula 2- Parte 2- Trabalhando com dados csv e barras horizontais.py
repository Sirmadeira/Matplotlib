import csv
import numpy as numpy
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


#Barras horizonstais sao mais recomendados com muito indexes x ae vc tranfere ppara o index y

plt.style.use('fivethirtyeight')
# Para dar call dos dados em panda escreva o seguinte
# data= pd.read_csv('dados.csv')
# ids= data['Responder_id']
# lang_responses = data[' LanguagesWorkedWith']

with open('dados.csv') as csv_pasta:
	csv_reader = csv.DictReader(csv_pasta)
# Voce teria que retirar essa parte

	language_counter= Counter()

	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))
# E escrever essa linha da seguinte maneira
#for response in csv_reader:
	#language_counter.update(response.split(';'))

lingua = []
popularidade = []

for item in  language_counter.most_common(15):
	lingua.append(item[0])
	popularidade.append(item[1])

lingua.reverse()
popularidade.reverse()
# Isso faz com que a lista seja revertida, alinhando o eixo y de cima para baixo (maiores para menores) e nao de baixo para cima que nem seria o tipico

plt.barh(lingua,popularidade) 


plt.title("Linguas mais populares")
plt.xlabel("Numero de pessoas que as usam")

plt.tight_layout()

plt.show()
# Isso e como voce pegaria os dados se utilizando de bibliotecas comuns
# Basicamente isso pega os dados da pasta csv contabiliza eles atraves de um loop