

#project Slot Machine
#	Requirements:
#		-Pelo menos 3 rodas
#		-Usar classes
#		-Ter uma quantidade de créditos iniciais os quais aumentam e diminuem de créditos iniciais os quais aumentam e diminuem de acordo com os ganhos
#		-Poder apostar diferentes quantidades de créditos em casa jogada
#		-Ter diferentes

#print function
#scan function always return a string (we can convert it later)

#lists are declared with [] and we can store whateverr we want (we store objects)
#tuples are lists that can't be changed declared with (), values can be accessed individualy 

# dictionary = {	"key1": "value1", "key2": 2, 3:False}

#functions declarration : def

#creating our own class
from random import randrange
import random

random.seed()

class Dice:
	sides = 6
	top_side = 1
	def __init__(self,sides):
		self.sides = sides
		self.top_sides = self.roll()
	def roll(self):
		return self.top_side = randrange(1,self.sides+1)

our_dice = Dice(20)
our_dice.roll()
print(our_dice.top_side)


#from time import localtime
#def f_exercise(n):
#	while n < 101 :



#		if ((n % 3) == 0) and ((n % 5) == 0) :
#			print("Hackerschool")
#		elif (n % 3) == 0 : 
#			print("Hacker")
##		elif n % 5 == 0:
#			print("School")
#		else:
#			print(n)
#		n += 1
#
#f_exercise(1)

#now = localtime()
#print (str(now))


























