def show_menu():
    print("==================================")
    print("Welcome to Just a normal FPS game!")
    print("==================================")
    
    
def show_options():
    print("- Play: Play the normal game!")
    print("- Tutorial: Understand how to play the game!")
    print("- Free Play: Play the game with every weapon and infinite waves!")
    print("- Exit: Exit the game!")
 
    

def show_Play():
    print("==================================")
    counter = 0
    gunpickup = int(input("Ready to play the game? Press 1 to pick up the gun or 2 to exit! "))
    if gunpickup == 1:
                    while counter != 5:
                        print("- Move: Press 1 to move in a random direction!")
                        print("- Shoot: Press 2 to shoot an enemy!")
                        moves =  int(input("What do you want to do? "))
                        if moves == 1:
                            counter += 1
                            print("You move north, east, south or west!")
                        elif moves == 2:
                            counter += 1
                            print("You shoot an enemy!")
                        else:
                             print("Invalid option!")
                    print("Game Over!")
                    main()

    if gunpickup == 2:
         main()

def show_Tutorial():
     print("==============================")
     print("===========Tutorial===========")
     print("- Move: Press 1 to move in a random direction!")
     print("- Shoot: Press 2 to shoot an enemy!")

def show_freeplay():
     print("==================================")
     choice1 = input("Welcome to free play! Would you like to choose between weapons or exit? (Weapons or Exit are the choices)")
     if choice1 == "Weapons":
          choice2 = input("What weapon would you like to choose? Pick a number: (1 - Machine Gun, 2 - Submachine Gun, 3 - Shotgun, 4 - Pistol, 5 - Rocket Launcher")
          if choice2 == 
    

def main():
    show_menu()
    show_options()

    choice = str(input("Choose from Play, Tutorial, Free Play, or Exit! "))
    
    if choice == "Play":
        show_Play()
    elif choice == "Tutorial":
        show_Tutorial()
    elif choice == "Free Play":
         print("free play tnime")

main()