def show_menu():
    """Displays the main menu of the game."""
    print("==================================")
    print("Welcome to Just a normal FPS game!")
    print("==================================")
    
    
def show_options():
    """Displays the options available in the game."""
    print("- Play: Play the normal game!")
    print("- Tutorial: Understand how to play the game!")
    print("- Free Play: Play the game with every weapon and infinite waves!")
    print("- Exit: Exit the game!")
 
    

def show_Play(main):
    """Starts the main game function."""
    print("==================================")
    counter = 0 # Counter to track moves (Will be changed to a health bar/wave counter)
    gunpickup = int(input("Ready to play the game? Press 1 to pick up the gun or 2 to exit! "))
    if gunpickup == 1: # If the player picks up the gun
                    while counter != 5: # While moves are less than 5
                        # Instructions
                        print("- Move: Press 1 to move in a random direction!")
                        print("- Shoot: Press 2 to shoot an enemy!")
                        moves =  int(input("What do you want to do? ")) # Asks the user for their choice
                        if moves == 1:
                            counter += 1 # Adds 1 to the counter every move
                            print("You move north, east, south or west!")
                        elif moves == 2:
                            counter += 1 # Adds 1 to the counter every move
                            print("You shoot an enemy!")
                        else:
                             print("Invalid option!")
                    print("Game Over!")
                    main() # Calls the main function again

    if gunpickup == 2: # Exit the game
         main()

def show_Tutorial(main):
     """Displays the tutorial for the game."""
     print("==============================")
     print("===========Tutorial===========")
     print("- Move: Press 1 to move in a random direction!")
     print("- Shoot: Press 2 to shoot an enemy!")
     main() # Calls the main function after viewing

def show_freeplay(main):
     """Starts the free play mode of the game."""
     print("==================================")
     choice1 = input("Welcome to free play! Would you like to choose between weapons or exit? (Weapons or Exit are the choices) ") # Choose between weapons or exit
     if choice1.lower() == "weapons":
          weapons = {1: "Machine Gun", 2: "Submachine Gun", 3: "Shotgun", 4: "Pistol", 5: "Rocket Launcher"} # Dictionary of weapons and numbers
          print("What weapon would you like to choose? Pick a number: (1 - Machine Gun, 2 - Submachine Gun, 3 - Shotgun, 4 - Pistol, 5 - Rocket Launcher ") # Asks the user for their choice
          choice2 = int(input("Enter the number of your choice: ")) # Input the weapon number
          if choice2 in weapons: # Check if the key is in the dictionary
                    print(f"You have chosen the {weapons[choice2]}!") # Prints the weapon name from the dictionary
                    while True: # Until the user exits because its free play
                        action = input("What would you like to do? (Move, Shoot or Exit) ") # Asks the user for their choice of action
                        # Actions that can be taken
                        if action.lower() == "move":
                                print("You move north, east, south or west!")
                        elif action.lower() == "shoot":
                                print("You shoot an enemy!")
                        elif action.lower() == "exit":
                                main()
                        else:
                             print("Invalid option!")
                             show_freeplay() # Calls the show_freeplay function again
          else:
                    print("Invalid choice! Please try again.")
                    show_freeplay() # Calls the show_freeplay function again
     elif choice1.lower() == "exit": # If exit is chosen
            main() # Calls the main function again