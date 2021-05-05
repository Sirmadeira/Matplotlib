import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Bins sao basicamente o local de deposito onde a data cai, e bom para acumular grandes quantidades de dados
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins=[10,20,30,40,50,60]

#Log basicamente distribui quando tem grandes quantidades de dados
# Essa aula n tem data porque era dados excessivos
plt.hist(ages,bins=bins,edgecolor='black', log= True )

idade_media= 29
# Cria uma lina vertical que demonstra a mediana
plt.axvline(idade_media, color='black', label='Idade media')

plt.title('Idades dos resspondentes')
plt.xlabel('Idades')
plt.ylabel('Total Respondentes')

plt.tight_layout()

plt.show()