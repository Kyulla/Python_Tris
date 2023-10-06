#Funzione che parte ad ogni inizio turno, serve a "pulire" il terminale dal turno precedente
def newTurn(position):
	for i in range(0,20):
		print("\n")
	grid(position)

#Funzione atta a verificare che la scelta sia valida all'interno del ciclo while per la selezione del nome, uso la funzione lower() per evitare il case sensitive
def playerNames():
	choice = input("Benvenuto "+players[i]+", vuoi scegliere un altro nome o lasciare quello di default?\n(C/c = cambia o D/d = default): ")
	choice = choice.lower()
	return choice

#Funzione che parte insieme alla funzione newTurn(), manda a video la griglia con le varie posizioni
def grid(position):
	for i in range(1,11):
		if i == 1 or i == 4 or i == 7 or i == 10:
			print("|_____|_____|_____|")

		elif i == 3:
			print("| ",position[0]," | ",position[1]," | ",position[2]," |")

		elif i == 6:
			print("| ",position[3]," | ",position[4]," | ",position[5]," |")

		elif i == 9:
			print("| ",position[6]," | ",position[7]," | ",position[8]," |")

		else:
			print("|     |     |     |")


#Funzione per la verifica della selezione della posizione del giocatore
def positionSelection(players, playerTurn, roles, position):
	turn = False

	try:
		movePosition = int(input("\n\nTurno di "+players[playerTurn]+", seleziona dove posizionare la/lo '"+roles[playerTurn]+"': "))

	except:
		print("Errore, non hai digitato un numero.")
		return turn

	#For per controllare ogni numero in lista
	for numPosition in position:
		#Una volta trovato il numero in lista equivalente a quello selezionato, lo andiamo a sostituire con il corrispettivo segno (X/O)
		if movePosition == numPosition:
			position[movePosition-1] = roles[playerTurn]
			turn = True
			return turn

	#In caso contrario, avvisiamo all'utente dell'errore e andremo a chiedere un'altra volta la posizione da selezionare
	if not turn:
		print("Errore, posizione scelta non valida.")
		return turn




#Funzione che controlla ad ogni turno se qualcuno ha vinto
def gameStatus(position, roles, playerTurn):

	#Controllo vittoria orizzontale
	if position[0] == roles[playerTurn] and position[1] == roles[playerTurn] and position[2] == roles[playerTurn]:
		return True

	elif position[3] == roles[playerTurn] and position[4] == roles[playerTurn] and position[5] == roles[playerTurn]:
		return True

	elif position[6] == roles[playerTurn] and position[7] == roles[playerTurn] and position[8] == roles[playerTurn]:
		return True



	#Controllo vittoria verticale
	elif position[0] == roles[playerTurn] and position[3] == roles[playerTurn] and position[6] == roles[playerTurn]:
		return True

	elif position[1] == roles[playerTurn] and position[4] == roles[playerTurn] and position[7] == roles[playerTurn]:
		return True

	elif position[2] == roles[playerTurn] and position[5] == roles[playerTurn] and position[8] == roles[playerTurn]:
		return True



	#Controllo vittoria obliqua
	elif position[0] == roles[playerTurn] and position[4] == roles[playerTurn] and position[8] == roles[playerTurn]:
		return True

	elif position[2] == roles[playerTurn] and position[4] == roles[playerTurn] and position[6] == roles[playerTurn]:
		return True


	#In caso di nessuna vittoria, mandiamo un false
	else:
		return False

#Inizializzazione di variabili varie
gameOver = False
position = [1,2,3,4,5,6,7,8,9]
players = ["Giocatore 1", "Giocatore 2"]
roles = ("X", "O")
playerTurn = -1
turns = 0

#Scelta del nome dei giocatori
for i in range(0,2):
	playerSelection = False

	#Il while di cui parlavo nella funzione playerNames()
	while not playerSelection:
		choice = playerNames()

		if choice == "d":
			playerSelection = True

		elif choice == "c":
			players[i] = input("Inserisci il nome desiderato: ")
			playerSelection = True

		else:
			print("Errore, risposta non valida.")

#Inizio vero e proprio del gioco
while not gameOver:
	#Nuovo loop, nuovo turno
	newTurn(position)
	turn = False
	playerTurn += 1

	#Ogni volta che finisce il giocatore 2 (il cui valore nella lista corrisponde all'int 1), verrà resettato il contatore del turno giocatore
	if playerTurn == 2:
		playerTurn = 0

	#While a funzione per controllare che la scelta della posizione selezionata dal giocatore sia valida
	while not turn:
		turn = positionSelection(players, playerTurn, roles, position)

	#Finito il turno, aumentiamo il contatore dei turni TOTALI e se, con questo turno, il giocatore ha vinto
	turns += 1
	vittoria = gameStatus(position, roles, playerTurn)

	#In caso di vittoria, partirà questo print
	if vittoria == True:
		newTurn(position)
		print("Ha vinto "+players[playerTurn]+"!")
		gameOver = True

	#In caso si dovessero utilizzare tutti i 9 turni senza vincitore, uscirà questo print
	elif turns == 9 and vittoria == False:
		newTurn(position)
		print("Pareggio.")
		gameOver = True
