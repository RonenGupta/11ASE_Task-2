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
    while counter != 5:
        gunpickup = int(input("Ready to play the game? Press 1 to pick up the gun or 2 to exit!"))
        if gunpickup == 1:
            print("-Move: Move in north, east, south or west")
            print("-Shoot: Shoot an enemy!")
            firstmove =  input("What do you want to do first?")
            if firstmove == 1:
                counter += 1
                print("You move north, east, south or west!")
            elif firstmove == 2:
                counter += 1
                print("You shoot an enemy!")
        




def main():
    show_menu()
    show_options()

    choice = str(input("Choose from Play, Tutorial, Free Play, or Exit!"))
    
    if choice == "Play":
        show_Play()
    elif choice == "Tutorial":
        print("shoing turoail")

main()