import  pandas as pd
from  matplotlib import  pyplot as plt

# plt.gcf()
# plt.gca()

plt.style.use('seaborn')
data = pd.read_csv('data.csv')
ages= data['Age']
dev_salaries = data ['All_Devs']
py_salaries = data ['Python']
js_salaries =data ['JavaScript']


fig,(ax1,ax2,ax3) =plt.subplots(nrows=3,ncols=1,sharex=True,sharey=True)

# fig1,ax1 =plt.subplots()
# fig2,ax2 =plt.subplots()
# fig3,ax3 =plt.subplots()

ax1.plot(ages,dev_salaries,color= 'darkblue',linestyle ='--',label='All Devs')
ax2.plot(ages,py_salaries,label ='Python')
ax3.plot(ages,js_salaries,label='JavaScript')



ax1.legend()
ax1.set_title('Employees Median salaries')
ax1.set_xlabel('Emloyees ages')
ax1.set_ylabel('Average Salaries')


ax2.legend()
ax2.set_xlabel('Emloyees ages')
ax2.set_ylabel('Average Salaries')
ax2.set_title('Employees Median salaries')

ax3.legend()
ax3.set_title('Employees Median salaries')
ax3.set_xlabel('Emloyees ages')
ax3.set_ylabel('Average Salaries')


# fig3.savefig('JavaScript')
# fig2.savefig('All Devs')
# fig1.savefig('Python')

fig.savefig('All three')


plt.tight_layout()
plt.show()
