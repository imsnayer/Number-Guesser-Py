from time import time
from random import randint

class Game:

		def __init__(self):
			pass
			
		def main(self):
			print("Welcome to Snayer's Number Guessing Game")
			self.getLevel()
		
		def getLevel(self):
			self.highest_num = raw_input("Enter highest number: ")
			try:
				val = int(self.highest_num)
				self.playGame()
			except ValueError:
				print("That's not a number!")
				self.getLevel()
		
		def playGame(self):
			self.time_begin = time()
			while True:
				self.answer = randint(1, int(self.highest_num))
				self.choice = int(raw_input("Enter Number: "))
				if self.choice < self.answer:
					print("Your number is too low!")
				elif self.choice > self.answer:
					print("Your number is too high!")
				else:
					print("You guessed the number!")
					self.time_end = time()
					self.TotalTime = str(int(self.time_end - self.time_begin))
					print("It took you %s seconds") % self.TotalTime
					print("\n\n")
					self.main()

if __name__ == "__main__":
		ObjG = Game()
		ObjG.main()
