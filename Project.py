#Projeto slot machine

import random

def symbol(slot):
	for i in range (3):
		if ( 0<= slot[i] <= 49):
			slot[i] = "#"
		elif (50 <= slot[i] < 90):
			slot[i] = "$"
		elif (90 <= slot[i] < 120):
			slot[i] = "%"
		elif (120 <= slot[i] < 140):
			slot[i] = "&"
		elif (140 <= slot[i] < 150):
			slot[i] = "@"
		elif (150 <= slot[i] < 155):
			slot[i] = "£"
		elif (slot[i] == 156):
			slot[i] = "€"
	return slot




def prize(ourslot, bet):
	if ( ourslot.slot[0] == "#"):
		return (5 * bet)
	elif (ourslot.slot[0] == "$"):
		return (10 * bet)
	elif (ourslot.slot[0] == "%"):
		return (20 * bet)
	elif (ourslot.slot[0] == "&"):
		return (70 * bet)
	elif (ourslot.slot[0] == "@"):
		return (200 * bet)
	elif (ourslot.slot[0] == "£"):
		return (1000 * bet)
	elif (ourslot.slot[0] == "€"):
		return (100000 * bet)
	else:
		return 0


def slot_machine(bet,credit):
	#slot = [0 for i in range (3)]
	#slot[0] = random.randint(0,100)
	#slot[1] = random.randint(0,100)
	#slot[2] = random.randint(0,100)
	#symbol(slot)
	ourslot = slot_symbols()
	ourslot.atri_value()
	print (slot_symbols.slot)
	if (ourslot.slot[0] == ourslot.slot[1]) and (ourslot.slot[0] == ourslot.slot[2]):
		credit += prize (ourslot, bet)
		print("Prémio: ", prize(ourslot,bet))
		print("Crédito atualizado: ",credit)
	else:
		print("Sem prémio \n")
	return credit

class slot_symbols:
	slot = [0 for i in range (3)]
	def atri_value(self):
		self.slot[0] = int(random.randint(0,156))
		self.slot[1] = int(random.randint(0,156))
		self.slot[2] = int(random.randint(0,156))
		for i in range (3):
			if ( 0<= self.slot[i] <= 49):
				self.slot[i] = "#"
			elif (50 <= self.slot[i] < 90):
				self.slot[i] = "$"
			elif (90 <= self.slot[i] < 120):
				self.slot[i] = "%"
			elif (120 <= self.slot[i] < 140):
				self.slot[i] = "&"
			elif (140 <= self.slot[i] < 150):
				self.slot[i] = "@"
			elif (150 <= self.slot[i] < 155):
				self.slot[i] = "£"
			elif (self.slot[i] == 156):
				self.slot[i] = "€"

#main fucntion


credit = int (input("Quantos créditos deseja depositar? "))
play = input("\ny para rodar n para parar de jogar: ")
while play != "n" :
	if (play != "y") and (play != "n"):
		print("Please enter a valid option!! y(es) OR n(o)")
	elif (play == "y") and (credit > 0):
			bet = int(input("Créditos a apostar: "))
			credit -= bet
			if (credit < 0):
				print("Quantia indisponível!")
				credit += bet
			else:
				credit = slot_machine(bet,credit)
	elif (credit == 0):
		print("You run out of money!")
		break
	play = input("\ny para rodar n para parar de jogar: ")
	






























