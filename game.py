import random
# ELECCIONES DE LA COMPUTADORA
computerChoices = ["tijera", "papel", "piedra"]

aleatorio = random.randint(0, (len(computerChoices) -1))


def juego():
    counter = 0
    # REGISTRO DE LOS PUNTOS POR JUGADOR
    ties = 0
    computerTries = 0
    userTries = 0
    # AQUÍ EMPIEZA EL JUEGO
    print("Bienvenido al juego de \'piedra, papel o tijera' ")
    while(counter < 3):
        # SECCION DE SELECCIÓN USUARIO
        userInput = input("Por favor escriba la opcion que le apetezca entre piedra, papel o tijera :")
        # VALORES DE LA SELECCIÓN DE AMBOS JUGADORES PARTA DEBUGGEAR
        # print(userInput)
        # print(computerChoices[aleatorio])
        # bloque de posibilidades
        if(userInput == 'tijera' and computerChoices[aleatorio] == "papel"):
            userTries += 1    
            counter += 1
            print("El usuario lleva  ",  userTries, " ganada(s)")
        elif(userInput == 'papel' and computerChoices[aleatorio] == "piedra"):
            counter += 1
            userTries += 1
            print("El usuario lleva  ", userTries, " ganada(s)")
        elif(userInput == 'piedra' and computerChoices[aleatorio] == "tijera"):
            counter += 1
            userTries += 1
            print("El usuario lleva ", userTries, " ganada(s)")
        elif(userInput == 'papel' and computerChoices[aleatorio] == "tijera"):
            counter += 1
            computerTries += 1
            print("El computador lleva", computerTries, " ganada(s)")
        elif(userInput == 'piedra' and computerChoices[aleatorio] == "papel"):
            counter += 1
            computerTries += 1
            print("El computador lleva ", computerTries, "ganada(s)")
        elif(userInput == 'tijera' and computerChoices[aleatorio] == "piedra"):
            counter += 1
            computerTries += 1
            print("El computador lleva ", computerTries, "ganada(s)")
        else:
            ties += 1
            print("Empatados")
            counter += 0

    print("El juego se llevó a cabo en", counter, " intentos y ", ties ," empates")

    if(userTries > computerTries):
        print("Este fueron los aciertos del usuario : ", userTries)
    if(userTries < computerTries):
        print("Este fueron los aciertos de la computadora : ", computerTries)
    


juego()

