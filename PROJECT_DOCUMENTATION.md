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
***
## Review
***
# Sprint 2
