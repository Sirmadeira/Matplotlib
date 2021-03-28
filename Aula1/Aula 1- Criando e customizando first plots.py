from matplotlib import pyplot as plt 


plt.style.use('ggplot')

plt.xkcd()
# Se voce quiser verificar os estilos disponiveis escreva o seguinte comando print('plt.style.available')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]


dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


plt.plot(ages_x,dev_y, color='k',linestyle= '--',marker='.', label = 'All devs')



py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, color='b' ,label='Python' ,linewidth='3', marker= 'o')

# Existe cores em formato red green blue como  #444444  e #5a7d9a


js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


plt.plot(ages_x,js_dev_y, color= '#444444',linewidth='3', label= 'Javascript')


plt.xlabel('Ages')
plt.ylabel('Median salary (USD)')
plt.title('Media salary (usd) by age')


plt.grid()
# Disponibiliza grid
plt.legend()
#Possibilita uso de legendas

plt.tight_layout()
#Focaliza layout
plt.savefig('plot_aula1.png')
#Salva a figura instantaneamente
plt.show()
