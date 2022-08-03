import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
age =data['Age']
dev_salaries = data['All_Devs']
py_salary = data['Python']
ja_salary= data ['JavaScript']

plt.plot(age,dev_salaries, color='#444444',linestyle='--',label='All_devs')
plt.plot(age,py_salary,label='python')
plt.plot(age ,ja_salary,label = 'JavaScript' ,color= 'Green',linestyle='-.')

overall_median=  74464

plt.fill_between(age,py_salary,dev_salaries,where=(py_salary>dev_salaries),color='#FFB90F',interpolate=True,alpha=0.25,label='Above average')


plt.fill_between(age,py_salary,dev_salaries,where=(py_salary<=dev_salaries),color='red',interpolate=True,alpha=0.25,label='Below average')

plt.fill_between(age,ja_salary,dev_salaries,where=(ja_salary>dev_salaries),color="darkblue",interpolate=True,alpha=0.25,label='Javasct Above average')

plt.fill_between(age,ja_salary,dev_salaries,where=(ja_salary<=dev_salaries),color='#00B2EE',interpolate=True,alpha=0.25,label='Javasct Above average')

plt.savefig('salary_1.png')
plt.legend()
plt.title('Median salary (usd) by age')
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.tight_layout ()
plt.show()