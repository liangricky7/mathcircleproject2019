from matplotlib import pyplot as plt
import random as rnd
import numpy as np


def three_player_flipp(p1_bal:int, p2:int, p3:int):
	
	rounds_elapsed = 0
	elapse_history = [0]
	p1_hist = [10]
	p2_hist = [10]
	p3_hist = [10]
	p1_bal = 10
	p2_bal = 10
	p3_bal = 10
	while (p1_bal != 0 and p2_bal != 0 and p3_bal != 0):
		#3 player condition
			rolling = rnd.randint(1,3)
			#player 1's roll win condition
			if rolling == 1:
				p1_bal += 2
				p2_bal -= 1
				p3_bal -= 1
				#updating rounds elapse
				rounds_elapsed += 1
				elapse_history.append(elapse_history[-1] + 1)
				#updating the balances
				p1_hist.append(p1_bal)
				p2_hist.append(p2_bal)
				p3_hist.append(p3_bal)
			#player 2's roll win condition	
			elif rolling == 2:
				p1_bal -= 1
				p2_bal += 2
				p3_bal -= 1
				#updating the x val
				rounds_elapsed += 1
				elapse_history.append(elapse_history[-1] + 1)
				#updating the y val
				p1_hist.append(p1_bal)
				p2_hist.append(p2_bal)
				p3_hist.append(p3_bal)
			#player 3's roll win condition
			else:
				p1_bal -= 1
				p2_bal -= 1
				p3_bal += 2
				#updating the x val		
				rounds_elapsed += 1
				elapse_history.append(elapse_history[-1] + 1)
				#updating the y val
				p1_hist.append(p1_bal)
				p2_hist.append(p2_bal)
				p3_hist.append(p3_bal)
#2 player conditions
	while p1_bal == 0:
		#player 1 death
		rolling_2 = rnd.randint(1, 6)
		if p2_bal == 0:
			print("Player 3 has won!")
			print(f"DEBUG 1: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()

		elif p3_bal == 0:
			print("Player 2 has won!")
			print(f"DEBUG 2: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()
		
		elif rolling_2 == 1 or rolling_2 == 2 or rolling_2 == 3:
			p2_bal += 1
			p3_bal -= 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(0)
			p2_hist.append(p2_bal)
			p3_hist.append(p3_bal)
			
		else:
			p2_bal -= 1
			p3_bal += 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(0)
			p2_hist.append(p2_bal)
			p3_hist.append(p3_bal)
	#player 2 death
	while p2_bal == 0:
		rolling_2 = rnd.randint(1, 6)
		if p1_bal == 0:
			print("Player 3 has won!")
			print(f"DEBUG 3: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()
		elif p3_bal == 0:
			print("Player 1 has won!")
			print(f"DEBUG 4: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()				
		elif rolling_2 == 1 or rolling_2 == 2 or rolling_2 == 3:
			p1_bal += 1
			p3_bal -= 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(p1_bal)
			p2_hist.append(0)
			p3_hist.append(p3_bal)
		else:
			p1_bal -= 1
			p3_bal += 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(p1_bal)
			p2_hist.append(0)
			p3_hist.append(p3_bal)	


	#player 3 death
	while p3_bal == 0: 
		rolling_2 = rnd.randint(1, 6)
			
		if p1_bal == 0:
			print("Player 2 has won!")
			print(f"DEBUG 5: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()			
		
		elif p2_bal == 0:
			print("Player 1 has won!")
			print(f"DEBUG 6: {len(elapse_history)}, {len(p1_hist)}, {len(p2_hist)}, {len(p3_hist)}")
			plt.plot(elapse_history, p1_hist, label = "Player 1")
			plt.plot(elapse_history, p2_hist, label = "Player 2")
			plt.plot(elapse_history, p3_hist, label = "Player 3")
			plt.legend()
			plt.show()		
			
		elif rolling_2 == 1 or rolling_2 == 2 or rolling_2 == 3:
			p1_bal += 1
			p2_bal -= 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(p1_bal)
			p2_hist.append(p2_bal)		
			p3_hist.append(0)
		else:
			p1_bal -= 1
			p2_bal += 1
			rounds_elapsed += 1
			elapse_history.append(elapse_history[-1] + 1)
			p1_hist.append(p1_bal)
			p2_hist.append(p2_bal)
			p3_hist.append(0)
		
three_player_flipp(1, 1, 1)
