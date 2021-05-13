import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# Esses graficos tem o proposito de demonstrar um conjunto de dados de acordo com o tempo
#dates = [
    #datetime(2019, 5, 25),
    #datetime(2019, 5, 24),
    #datetime(2019, 5, 26),
    #datetime(2019, 5, 27),
    #datetime(2019, 5, 28),
    #datetime(2019, 5, 29),
    #datetime(2019, 5, 30)
#]

#y = [0, 1, 3, 4, 6, 5, 7]

#Linestyle = solid basicamente garante que o conjunto de dados seja feito em linhas ao inves de pontos

#plt.plot_date(dates,y, linestyle='solid')

# Get current figure, pega a imagem atual, e acrescente  nova mecanica nesse caso ela insere um alinhamento no formato de data e deixa alinhado

#plt.gcf().autofmt_xdate()

# Isso daki basicamente formata a data para que tenha mes primeiro dia segundo ano terceirro
#date_format = mpl_dates.DateFormatter('%b, %d,%y')
# Esse codigo get current axis ou pega o axis da imagem, sendo esse o x e define o formato de data para o date_format definido anteriormente
#plt.gca().xaxis.set_major_formatter(date_format)

data = pd.read_csv('data.csv')


# Isso daki e uma funcao panda que transforma as strings em datetimes, basicamente para evitar erros de ordem esquisita

data['Date'] = pd.to_datetime(data['Date'])

data.sort_values('Date', inplace= True)


price_date = data['Date']
price_close = data['Close']

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.gcf().autofmt_xdate()

plt.plot_date(price_date,price_close, linestyle='solid')

plt.tight_layout()

plt.show()