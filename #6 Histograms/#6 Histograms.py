import  pandas as pd
from  matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

data=pd.read_csv('data.csv')
ids= data['Responder_id']
ages=data['Age']


bins=[0,10,20,30,40,50,60,70,80,90,100,110]
plt.hist (ages,bins=bins,edgecolor= "black",log=True,label='Respondents')

median_age=29
color= 'red'

plt.axvline(median_age,color=color,label='Age of median',linewidth=1.5)


plt.legend()






plt.title ('Age respondents')
plt.xlabel('Ages b/w')
plt.ylabel("Total respondentd")
plt.tight_layout()
plt.show()