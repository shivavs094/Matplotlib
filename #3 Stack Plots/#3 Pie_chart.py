import matplotlib.pyplot as plt
from matplotlib import pyplot
# plt.style.use('fivethirtyeight')
plt.xkcd()

slices=[53587, 46259, 39792, 38835, 29162]
labels=['JavaScript', 'HTML/CSS', 'Python', 'SQL', 'Java']
colors=['#EE6A50','#FFB90F','#00B2EE','#00FF00',	'#FF69B4']
explode=[0.1,0.1,0.1,0.1,0.1]

plt.pie (slices,labels=labels,explode=explode,shadow=True,startangle=20,autopct='%1.1f%%' ,colors=colors,wedgeprops={'edgecolor':'black'})


plt.savefig('Mat_1.png')
plt.title("Pie chart")
plt.tight_layout()
plt.show()


