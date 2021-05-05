import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

#Isso daki basicamente preenche os valores que estao acima da linha media em azul
plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')
#isso daki e mesma coisa mas para o a diferenca que esta abaixo da ,media, interpolate basicamente garante a qualidade do prenchimento para ele n ultrapassar o x axis
plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Diferenca de salario por idade')
plt.xlabel('idades')
plt.ylabel('Salario medio)')

plt.tight_layout()

plt.show()