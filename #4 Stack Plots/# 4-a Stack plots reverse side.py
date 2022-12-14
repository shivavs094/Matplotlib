from matplotlib import pyplot as plt

# plt.style.use("fivethirtyeight")
plt.xkcd()

minutes=[1,2,3,4,5,6,7,8,9]

player1= [8,6,5,5,4,2,1,1,0]
player2= [-1,1,2,2,2,4,4,4,4]
player3= [0,1,1,2,2,2,3,3,4]
colors=['#EE6A50','#FFB90F','#00B2EE']
labels=['player1','player2','player3']
# plt.pie([1,1,5], labels=["player1","player2","player3"] )

plt.stackplot(minutes,player1,player2,player3 ,labels=labels,colors=colors)
plt.savefig('Stac_a.png')
plt.title("My pie chart")
plt.legend(loc=(0.07,0.05))
plt.tight_layout()
plt.show()