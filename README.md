# Gebeta
Term Project [15112]

# Author: Temesgen Tewolde

1.Project Description:
* **Gebeta** is one of the oldest board games in the world. The objective of this project is to develop a web-based version of Gebeta that allows users to play against each other in a single account or against the computer. The project might also include a multiplayer mode.  

2. Competitive Analysis:
* While researching Gebeta games, the author came across a mobile app with a complicated GUI and multiple levels. This project will be inspired by the mobile app, but it will implement the Ethiopian version of the game. The project will include concise instructions on how to play the game, and if possible, an in-game instruction window.


3. Structural Plan:
* The project will have 3 major components:
    View: This will include the GUI component, which will have the following features:
        - Title of the game
        - Label indicating the current player
        - Label indicating which row belongs to which player (Player 1 and Player 2)
        - Button that reads 'Click here for instructions'
        - Buttons representing the small holes with the text indicating the number of marbles in each hole
        - Labels of slightly larger size for the two big buckets
        - Button that allows for restart

    Model: This will be the game engine itself, including alpha-beta pruning and the multiplayer option, using lessons learned in network programming.
    Controller: This will connect the View and Model components.

    If possible, the author will add the following features to the GUI:
    - In-game move-by-move instructions
    - Sound and/or music option
    - Change the image of the buttons to the number of marbles using free marble vectors and Adobe Illustrator to create copies of them

4. Algorithmic Plan:
* The author will use alpha-beta pruning to allow a user to play against the computer. The static evaluation on the final positions will consider the number of marbles in the big bucket, with a higher number of marbles being better for the chosen player. If the number of marbles in the opposition's big bucket is larger than the chosen player's, the static evaluation will yield a negative result.

5. Timeline Plan:
* By the end of Week 12: Build the GUI and study alpha-beta pruning
* By the end of Week 13: Develop a working project that allows users to play against the computer
* By the end of Week 14: Continue working on the alpha-beta pruning implementation and begin working on the multiplayer option
                         
6. Version Control Plan: 
* The author will upload the project on GitHub and use version control tools according to best practices advised by professionals.

7. Module List: I will not be using any external modules/hardware/technologies.

