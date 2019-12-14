from random import randint

#Bienvenida
print("Hi! let's play a game, I will think about one number between 0 and 20 and you should guess it.\nDon't worry, I'll help you.")

#Empieza el juego
while True:
	Number=randint(0,20)
	while True: 
		try: guess=int(input("\nIn which number I'm thinking about?: "))
		except ValueError: 
			print("Sorry, enter a valid number.") 
			continue
		else: break
	while(Number!=guess):
		if(guess<Number): 
			while True: 
				try: guess=int(input("Too low! Try again: "))
				except ValueError: 
					print("Sorry, enter a valid number.") 
					continue
				else: break
		else: 
			while True: 
				try: guess=int(input("Too high! Try again: "))
				except ValueError: 
					print("Sorry, enter a valid number.") 
					continue
				else: break
	replay=0
	while(replay!='Y' and replay!='N'):
		replay=input("\nYou got it!! The number was "+ str(Number) +". Do you want to try again? (y/n): ").upper()
	if(replay=='n'):
		break
	
print("\n\n 						GAME OVER")
input("\n\nPress ENTER to close the program...")