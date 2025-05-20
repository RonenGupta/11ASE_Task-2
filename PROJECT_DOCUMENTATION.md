# Year 11 Accelerated Software Engineering Assessment Task 2 - First Person Shooter 
### By Ronen

# Sprint 1
## Requirements Definition
***
### Functional Requirements

- Data Retrieval: The user must be able to view a gun or similar shooter on the side/middle of their screen, a crosshair in the middle.

- User Interface: The user must have a working PC or laptop with a keyboard, mouse and be aware on basic WASD and mouse clicking controls.

- Data Display: The user may be able to view kill count, ammo amount, possible a hotbar with weapons and ammo amounts corresponding to certain weapons, and other variables on the upper sides of the screen will have to be hidden.

***
### Non-Functional Requirements
- Performance: The system needs to load up in under 10 seconds, have at least above 100 FPS, and all functions must function.

- Reliability: The system must not include too many major bugs, and the data should be reliable in order to control realistic FPS physics.

- Usability and Accessibility: The system must be extremely easy to get a hold of. WASD, space and mouse controls will be the only controls for playing the game, and instructions can be directed from a README.
***
## Determining Specifications
***
### Functional Specifications
- User Requirements: The user must be able to move around and shoot with WASD, Jump and mouse controls as well as pick up and shoot a gun.

- Inputs and Outputs: Will need to accept keyboard controls such as WASD and Jump as well as left click and moving the mouse around.

- Core Features: The program must be able to provide a fun and enjoyable FPS game experience, with enemies and a wave based gamemode which the user can play in. There should be a custom map, guns to pick from, and different enemies that spawn with different abilities.

- User Interaction: Users can interact with the system through the Ursina module, notably used for python game making, and a README can be provided to help users navigate.

- Error Handling: The system may fail to launch, crash mid-way, or miscellaneous errors may occur from runtime to developer based issues during launch.
***
### Non-Functional Specifications

- Performance: The system should be able to load in less than 30 seconds, and user input must not be delayed and FPS should be high.

- Usability/Accessibility: Possibly add a UI main menu if supported in Ursina, tutorial tab, free play (If wanting to test all weapons, gamemodes). 

- Reliability: UI design and map design will be an issue, and miscalculations along the way would possibly occur in the development process, however these will be addressed firmly due to their difficulty.
***
### Use Case

- Actor: User (Gamer/FPS Game Fan)

- Preconditions: Internet access; required specs for game, modules installed, controls understood.

- Main Flow:

1. Launch Game: User launches the game and sees a menu screen with 4 tabs. Play, free play, tutorial, and exit.

2. Clicks Play: User clicks play (As it is the normal option) and spawns in a map with a gun on the floor, and on the UI appears his health and stamina bar.

3. Start Game: After user picks up the gun with a mouse click, the game starts and enemies come out wave by wave, with certain enemies coming in certain waves.

4. Game End: After the game has ended, (The user has died ingame) the game calculates the score of all the enemies that have been killed, and outputs them to the user in a UI.

5. Loop: The user is then prompted to the menu screen again with the same 4 tabs, leading to a loop until they press the exit button, where they can view the tutorial, free play, or play before exiting.

- Postconditions: User has played a gamemode, understands how to play the game and has viewed their score.

***
## Design
***
## Build and Test
### Sprint 1 - FPS Text Based GUI Modularized
- Sprint1Module.py
```python
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
```

- Sprint1.py
```python
from Sprint1Module import * # Imports all functions from the Sprint1Module

def main():
    """The main function that runs the text-based game."""
    show_menu() # Calls the show_menu function, displaying the menu
    show_options() # Calls the show_options function, displaying the options

    choice = str(input("Choose from Play, Tutorial, Free Play, or Exit! ")) # Asks the user for their choice
    
    if choice.lower() == "play": # Calls the show_Play function starts the game
        show_Play(main)
    elif choice.lower() == "tutorial": # Calls the show_Tutorial function, displays the tutorial
        show_Tutorial(main)
    elif choice.lower() == "free play": # Calls the show_freeplay function, starts free play
        show_freeplay(main)
    elif choice.lower() == "exit": # Calls the exit function, exits the game
        print("Thanks for playing!")
        exit()

main()
```
***
## Review
1. The program so far does not exactly follow the functional and non-functional requirements exactly, but provides a layout of what the finished program would possibly look like. This text based UI can be implemented into Ursina, as I have previously created a program suitable for the requirements of Sprint 2 with Ursina meeting most of the functional and non-functional requirements. So on and so forth, this program serves as a base for the finished product, being a text based GUI. I did not choose to do a UI based Sprint 1 due to Ursina's inbuilt Person class, which makes movement automatic and without the requirement of UI based buttons. I tried this and I found it useless, so I resorted to a text based GUI which allowed for a more dynamic approach to what would be the finished product. Sprint 2 may include some features from Sprint 1, but will not have all of them but will be in much better quality overall via Ursina Engine rendering.

2. The use case I created was perfectly replicated by the text based GUI I made, being incredibly similar in progression and only contains few minor changes (I made the main game end in 5 moves instead of waiting for the player to die as I would require Ursina). It takes input and produces output to a high standard, allowing for good behavourial replication.

3. Organisation and readability was distinctive in the text based GUI I made. With the use of modularization, docstrings, comments and function organisation/naming, it was simply impossible for not being able to understand the program. Overall, an outstanding use of quality in the GUI.

4. The next stage of development should immediately implement OOP and further complex aspects of classes. I had already created a base for Sprint 2 which I originally planned to be Sprint 1, however due to Sprint 1 requirements of text based GUI, I resorted to the main.py that is currently in the repository to be submitted as Sprint 2 after being modularised and tweaked a little more. This would add the inbuilt function for FPS controller, and I would also add a working gun (Pistol for now) and an interesting feature, a hookshot, allowing for the user to traverse quicker as if using a grapple gun, possibly a good idea for map design in the game. Overall, huge changes would occur when transitioning from text based to Ursina, and I would be ready to further enhance further from Sprint 2 onwards, adding distinctive gamemodes, UI and other functional/non-functional requirements that the game requires.
***
# Sprint 2
