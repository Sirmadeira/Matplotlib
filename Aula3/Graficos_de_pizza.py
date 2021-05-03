from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')
# Basicamente os x. y, z ... dos  graficos
pedacos= [60,40,30,20]
# Labels
titulos= ['Sessenta','Quarenta','Batata','Potato']
cores=['blue','red','yellow','green']
#Basicamente retira um pedacao da pizza e da mais destaque a ela
explode= [0,0,0.2,0]
# Maneira de configurar, as bordas
# Autopct basicamente serve para disponibilizar porcentagens
plt.pie(pedacos, labels=titulos,colors=cores,explode=explode,shadow=True,autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})

plt.title('Meu grafico de pizza')
plt.tight_layout()
plt.show()