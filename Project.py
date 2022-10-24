#Projeto slot machine

import random



class SlotSymbols:
	slot = [0 for i in range (3)]
	def atri_value(self):
		self.slot[0] = int(random.randint(0,155))
		self.slot[1] = int(random.randint(0,155))
		self.slot[2] = int(random.randint(0,155))
		for i in range (3):
			if 0 <= self.slot[i] < 50:
				self.slot[i] = "#"
			elif 50 <= self.slot[i] < 90:
				self.slot[i] = "$"
			elif 90 <= self.slot[i] < 120:
				self.slot[i] = "%"
			elif 120 <= self.slot[i] < 140:
				self.slot[i] = "&"
			elif 140 <= self.slot[i] < 150:
				self.slot[i] = "@"
			elif 150 <= self.slot[i] < 155:
				self.slot[i] = "£"
			elif self.slot[i] == 155:
				self.slot[i] = "€"
	def prize(self, bet):
		if self.slot[0] == "#":
			return (5 * bet)
		elif self.slot[0] == "$":
			return (10 * bet)
		elif self.slot[0] == "%":
			return (20 * bet)
		elif self.slot[0] == "&":
			return (70 * bet)
		elif self.slot[0] == "@":
			return (200 * bet)
		elif self.slot[0] == "£":
			return (1000 * bet)
		elif self.slot[0] == "€":
			return (100000 * bet)
		else:
			return 0
	def slot_machine(self,bet,credit):
		self.atri_value()
		print (self.slot)
		if self.slot[0] == self.slot[1] == self.slot[2]:
			credit += self.prize (bet)
			print("Prémio: ", self.prize(bet))
			print("Crédito atualizado: ",credit)
		else:
			print("Sem prémio \n")
		return credit

#main fucntion

if __name__ == "__main__":
	ourslot = SlotSymbols()
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
					credit = ourslot.slot_machine(bet,credit)
		elif (credit == 0):
			print("You run out of money!")
			break
		play = input("\ny para rodar n para parar de jogar: ")
	




