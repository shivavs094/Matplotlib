import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import  dates as mpl_dates

plt.style.use('seaborn')

data =pd.read_csv('data.csv')
pice_date=data['Date']
price_close= data['Close']

data['Data'] =pd.to_datetime(data['Date']) # to sort mixed date
data.sort_values('Data',inplace=True)





# date = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
# y=[0,1,3,4,6,5,7]

plt.plot_date(pice_date,price_close,linestyle='solid',label = 'Direction')
plt.gcf().autofmt_xdate()

# date_format=mpl_to

plt.legend()
plt.tight_layout()
plt.show()