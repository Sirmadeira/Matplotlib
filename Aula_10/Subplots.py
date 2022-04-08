import pandas as pd
from matplotlib import pyplot as plt

# Subplots servem para voce ter um controle mais exato do objeot que voce tem ou seja qual axis e qual, se vc quiser configurar mas diretamente figura geral etc.
plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1)

# Agora como voce pode ver eu posso dar mais legendas titulo para cada tracejado, tendo um controle mais imediato de cado tracejado, e definbindo cada um

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.legend()

ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()

ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()


plt.show()