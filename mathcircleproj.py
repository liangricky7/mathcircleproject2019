from matplotlib import pyplot as plt
import random as rnd
import numpy as np
#starting amount of money
x = [0]
y = [50]
def flipping_fair(n_simulations = 50):
#	amount of dollars	
	balance = 50

	for i in range(n_simulations):
		# marks bounds of gambling
		while 100 > balance and balance > 0:
			
			coin = rnd.randint(1, 100)
			# checks for coin flip's result
			if coin <= 50:
				balance += 1				
				x.append(x[-1]+1)
				y.append(balance + 1)
				print(balance)
			else:
				balance -= 1
				x.append(x[-1] +1 )
				y.append(balance - 1)
				print(balance)
	print()
	return balance


string = 'The end balance: '
print(string, (flipping_fair()))
plt.title("Gambler's Ruin: Fair")
# returns the last plotted point before termination
print(x[-1], y[-1])
plt.plot(x, y)
plt.show()


































