
# Go Fish with a Robot

This project is a terminal-based implementation of the Go Fish card game featuring an AI opponent. It is designed for anyone interested in playing around with AI. This project is being developed to help familiarize myself with AI integrations. The game deals cards, checks for matches, and manages gameplay between the player and the AI, providing a simple yet functional simulation of the Go Fish game.

I had ChatGPT write that description. It seemed fitting given the project. I wrote the preceding two sentences and this current one.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
## Authors

- [@codepapayas](https://www.github.com/codepapayas)


## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## Tech Stack

- **Python**: The primary programming language used for the game logic and AI integration.
- **OpenAI API**: Utilized for the AI opponent's decision-making process.
- **termcolor**: For colorizing the text output in the terminal.
- **prettytable**: For creating readable table displays of the player's and AI's hands.



## Environment Variables

To run this project, you will need your own OpenAI API key. 

` OPENAI_API_KEY `

## Project Outline: Go Fish Game in Python

#### 1. AI Logic
   - **Define AI Player Class**
     - Connect OpenAI to AI logic - ✅
     - Refine prompt for better results ~(currently rambling) - 🫠~ ✅

#### 2. Turn Logic
   - **Define Player Class**
     - Methods for player actions
     - Managing hand of cards - ✅
     
   - **Player Turn Function**
     - Structure of a player's turn
     - Asking for a card
     - Handling success or failure of the request
     
   - **Turn Transition**
     - Switching between players
     - Handling turn end conditions
     
   - **Turn Feedback**
     - Displaying results of each turn
     - Updating game state based on turn outcomes

#### 3. Game Logic
   - **Integrate Existing Components**
     - Utilize existing deck building, shuffling, dealing, and matched set removal logic - ✅
     
   - **Game Loop**
     - Main game loop to handle turns
     - Checking for game end conditions
       
   - **Game End Logic**
     - Determining the winner
     - Handling tie scenarios
     
   - **Score Keeping**
     - Tracking books collected by each player
     - Displaying final scores

#### 4. Integration
   - **Bringing it All Together**
     - Integrating AI, turn, and game logic into a cohesive game flow
     - Ensuring smooth transitions and interactions between components


