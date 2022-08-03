from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes=[1,2,3,4,5,6,7,8,9]

player1= [1,2,3,3,4,4,4,4,5]
player2= [1,1,1,1,2,2,2,3,4]
player3= [1,1,1,2,2,2,3,3,3]
colors=['#EE6A50','#FFB90F','#00B2EE']
labels=['player1','player2','player3']
# plt.pie([1,1,5], labels=["player1","player2","player3"] )

plt.stackplot(minutes,player1,player2,player3 ,labels=labels,colors=colors)

plt.title("My pie chart")
plt.savefig('Stac_1 .png')
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()