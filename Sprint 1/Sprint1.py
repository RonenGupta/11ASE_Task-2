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