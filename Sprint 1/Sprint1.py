from Sprint1Module import *

def main():
    show_menu()
    show_options()

    choice = str(input("Choose from Play, Tutorial, Free Play, or Exit! "))
    
    if choice.lower() == "play":
        show_Play(main)
    elif choice.lower() == "tutorial":
        show_Tutorial(main)
    elif choice.lower() == "free play":
        show_freeplay(main)
    elif choice.lower() == "exit":
        print("Thanks for playing!")
        exit()

main()