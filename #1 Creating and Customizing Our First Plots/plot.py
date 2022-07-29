from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
# plt.xkcd()
Age_x = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
dev_y = [5000, 6500, 7500, 10000, 12000, 15000, 25000, 30000, 40000, 45000, 60000, 70000, 80000, 100000, 150000]

plt.plot(Age_x, dev_y, '.c-', label='All Dev')

py_dev_y = [6000, 7500, 9500, 15000, 19000, 25000, 35000, 39000, 45000, 49000, 75000, 90000, 100000, 120000, 180000]


jav_dev_y = [6500, 8500, 9000, 15500, 20000, 27000, 35000, 38000, 46000, 50000, 75500, 92000, 120000, 125000, 180000]

plt.plot(Age_x, jav_dev_y,linewidth=2 ,color='red',linestyle = '--'  ,label='JAVA')  # for clolorind and styling parpuse ##fmt = '[marker][linestyle][color]'
plt.plot(Age_x, py_dev_y,color='darkblue',linestyle = '--' ,marker= '.' ,label='Python')  # for clolorind and styling parpuse ##fmt = '[marker][linestyle][color]'

plt.xlabel('Ages')
plt.ylabel('Median salary (INR)')
plt.title('Median salarty (USD) by Age')

plt.savefig('Mat_1.png')

plt.legend()
plt.tight_layout( )
# plt.grid(True)


plt.show()
print(plt.style.available)

