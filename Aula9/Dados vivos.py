import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Essa aula serve para destacar como lidar com plots de dados vivos ou que variam severamnete, e tem adicoes de novos dados 

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []



index = count()
# Aviso para qualquer um que venha aqui dps de mim, ctrl mais / descomenta codigos em grandes quantidades

def animate(i):
    #x_vals.append(next(index))
    #y_vals.append(random.randint(0, 5))
    # Isso daki e aquele dados que sao feito randomicamente
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    # Cuidado aqui sempre limpe o seu axis, pq senao as linhas vao ficar se sobrepondo e trocando de cor e fica bem zuadinho
    #Comente clear local axis, para ver como fica sem resetar eles

    plt.cla()

    plt.plot(x, y1, label='Canal 1')
    plt.plot(x, y2, label='Canal 2')
    # Esse codigo foi feito, para mostrar que as pequenas variacoes de um jeito menos distrativo	
    plt.legend(loc='upper left')
    plt.tight_layout()

# Isso daki e muito legal a consequencia disso e um grafico animado UHUHUHU
ani= FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


data = pd.read_csv('data.csv')
x = data['x_value']
y1 = data['total_1']
y2 = data['total_2']