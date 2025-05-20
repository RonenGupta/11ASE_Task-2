def show_menu():
    print("==================================")
    print("Welcome to Just a normal FPS game!")
    print("==================================")
    
    
def show_options():
    print("- Play: Play the normal game!")
    print("- Tutorial: Understand how to play the game!")
    print("- Free Play: Play the game with every weapon and infinite waves!")
    print("- Exit: Exit the game!")
 
    

def show_Play(main):
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

def show_Tutorial(main):
     print("==============================")
     print("===========Tutorial===========")
     print("- Move: Press 1 to move in a random direction!")
     print("- Shoot: Press 2 to shoot an enemy!")
     main()

def show_freeplay(main):
     print("==================================")
     choice1 = input("Welcome to free play! Would you like to choose between weapons or exit? (Weapons or Exit are the choices) ")
     if choice1.lower() == "weapons":
          weapons = {1: "Machine Gun", 2: "Submachine Gun", 3: "Shotgun", 4: "Pistol", 5: "Rocket Launcher"}
          print("What weapon would you like to choose? Pick a number: (1 - Machine Gun, 2 - Submachine Gun, 3 - Shotgun, 4 - Pistol, 5 - Rocket Launcher ")
          choice2 = int(input("Enter the number of your choice: "))
          if choice2 in weapons:
                    print(f"You have chosen the {weapons[choice2]}!")
                    while True:
                        action = input("What would you like to do? (Move, Shoot or Exit) ")
                        if action.lower() == "move":
                                print("You move north, east, south or west!")
                        elif action.lower() == "shoot":
                                print("You shoot an enemy!")
                        elif action.lower() == "exit":
                                main()
                        else:
                             print("Invalid option!")
                             show_freeplay()
          else:
                    print("Invalid choice! Please try again.")
                    show_freeplay()
     elif choice1.lower() == "exit":
            main()