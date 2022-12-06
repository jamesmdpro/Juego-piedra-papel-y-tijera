import random

options = ("piedra" , "papel", "tijera")

rounds = 1
computer_wins = 0
user_wins = 0

while True:


    print("*" * 20)
    print("ROUND", rounds)
    print("*" * 20)
    print("WINS PC", computer_wins)
    print("WINS USER", user_wins)

    user_option =  input("""
Escribe tu selección entre ( PIEDRA , PAPEL , TIJERA )

 """)
    computer_option = random.choice(options)
    user_option = user_option.lower()

    if not user_option in options:
        print ("Esa opcion no es valida")
        continue

    if user_option == computer_option:
        print("Juego Empatado")
    elif user_option == "papel" and computer_option == "tijera":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "papel" and computer_option == "piedra":
        print("le Ganaste a la computadora")
        user_wins += 1
    elif user_option == "tijera" and computer_option == "papel":
        print("le Ganaste a la computadora")
        user_wins += 1
    elif user_option == "tijera" and computer_option == "piedra":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "piedra" and computer_option == "papel":
        print("la computadora gana")
        computer_wins += 1 
    elif user_option == "piedra" and computer_option == "tijera":
        print("le Ganaste a la computadora")
        user_wins += 1

    if user_wins == 3:
        print("EL GANADOR ES EL USUARIO")
        break
    elif computer_wins == 3:
        print("LA COMPURADORA GANA")
        break

    rounds += 1

