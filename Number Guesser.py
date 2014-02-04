def start():
	print '-' * 40
	print "Welcome to Snayer's Guessing Game"
	print '-' * 40
	print "What difficutly do you want?"
	print "\t1. Easy: 1-10."
	print "\t2. Medium: 1-100."
	print "\t3. Hard: 1-1000.\n"
	choice = raw_input("> ")
	if choice == "1":
		easy()
	elif choice == "2":
		medium()
	elif choice == "3":
		hard()
	else:
		print "Please enter 1, 2, or 3 to select a difficutly."
		startfail() 
		
def startfail():
	print "What difficutly do you want?"
	print "\t1. Easy: 1-10."
	print "\t2. Medium: 1-100."
	print "\t3. Hard: 1-1000.\n"
	choice = raw_input("> ")
	if choice == "1":
		easy()
	elif choice == "2":
		medium()
	elif choice == "3":
		hard()
	else:
		print "Please enter 1, 2, or 3 to select a difficutly."
		startfail()
		
def easy():
	import random
	import time
	answer = random.randint(1,10)
	time1=time.time()
	while True:
		choice = int(raw_input(""))
		if choice < answer:
			print ("Too Low!")
		elif choice > answer:
			print ("Too High!")
		elif choice == answer:
			print ("You got it!")
			time2=time.time()
			TotalTime=str(int(time2-time1))
			print ("It took you " + TotalTime + " seconds.")
			again()
			
def medium():
	import random
	import time
	answer = random.randint(1,100)
	time1=time.time()
	while True:
		choice = int(raw_input(""))
		if choice < answer:
			print ("Too Low!")
		elif choice > answer:
			print ("Too High!")
		elif choice == answer:
			print ("You got it!")
			time2=time.time()
			TotalTime=str(int(time2-time1))
			print ("It took you " + TotalTime + " seconds.")
			again()
			
def hard():
	import random
	import time
	answer = random.randint(1,1000)
	time1=time.time()
	while True:
		choice = int(raw_input(""))
		if choice < answer:
			print ("Too Low!")
		elif choice > answer:
			print ("Too High!")
		elif choice == answer:
			print ("You got it!")
			time2=time.time()
			TotalTime=str(int(time2-time1))
			print ("It took you " + TotalTime + " seconds.")
			again()
			
def again():
	print ("Want to play again?")
	print "\t1. Yes."
	print "\t2. No."
	choice = raw_input("> ")
	if choice == "1":
		replay()
	elif choice == "2":
		exit()
		
def replay():
	print ("Oh cool. You must like this game then.")
	startfail()
start()
