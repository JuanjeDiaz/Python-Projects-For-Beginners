import random
hand=["Rock","Paper","Scissors"]

#Función que devuelve el mensaje de victoria, derrota o empate.

def result(P1,P2):
	win="YOU WIN!!"
	lose="YOU LOSE!!"
	draw="IT'S A DRAW"
	if(P1==P2): return(draw)
	if(P1=="Rock" and P2=="Scissors"): return(win)
	if(P1=="Paper" and P2=="Rock"): return(win)
	if(P1=="Scissors" and P2=="Paper"): return(win)
	else: return(lose)

#Empieza el juego

while(True):
	bot=random.choice(hand)
	while(True):
		player=input("Rock, Paper or Scissors?: ").capitalize()
		if(player in hand): break

	print((result(player,bot))+" You have chosen " +player.upper()+ " and the computer has chosen "+bot.upper()+".\n")