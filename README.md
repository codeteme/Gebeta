# Gebeta
Term Project [15112]

# Author: Temesgen Tewolde

1.Project Description:
* Gebeta
* Gebeta is one of the oldest board games in the world.
    The project will allow two users to play against each other in a single account.
    The project will allow a user to play against the computer.
    The project might also allow the users to play in multiplayer mode.

2. Competitive Analysis:
* I have came across a mobile app appropriately called Gebeta.
    It has a fairly complicated GUI and multiple levels.
    My project will be inspired by the game. First, the mobile app allows
    users to play the Ethiopian version of the game as opposed to the
    slightly tweaked international version of the game. The project will
    also implement the that particular version. The game will of course
    include a file with concise note on the instructions to play the game.
    If possible, I will try to add an in-game instruction in addition to a
    instruction-only window.

3. Structural Plan:
* The project will have 3 major components:
    View  - the GUI component (a detailed plan is written in the following paragraph)
    Model - the game engine itself
          - this is where alpha-beta pruning comes into picture and the multiplayer option
          (which I will make use of lessons learned in network programming), and
    Controller

    - Title of the game
    - Label that indicates the current player
    - Label that indicates which row belongs to which player. (Player 1 and Player 2)
    - Button that reads 'Click here for instruction'.
    - Button for the small holes will be buttons and the text will be the marbles in that hole.
    - Labels of slightly large sizes for the two big buckets.
    - Button that allows for restart.

    If possible I will add the following:
    - An in-game move-by-move instruction.
    - A sound and/or music option.
    - Change the image of the buttons to number of marbles. I can use the free marble vectors and
        use Adobe Illustrator to create copies of them.


4. Algorithmic Plan:
    I will employ alpha-beta pruning to allow a user to play against the computer.
    The static evaluation on the final positions would look at the number of marbles in the big bucket.
    In other words, the greater the number of marbles, the better the move is for the chosen player.
    If the number of marbles in the opposition's big bucket is larger than the chosen player's, then the
    static evaluation will yield a negative result (marbles in the big bucket of chosen player - marbles in big bucket of opposition player)

5. Timeline Plan:
* By the end of Week 12, I will have build the GUI. Meanwhile, I will be studying alpha-beta pruning.
* By the end of Week 13, I will have a working project that allows users to play against the computer.
* By the end of Week 14, I will continue working on the alpha-pruning implementation.
                         I will also begin working on multiplayer option.

6. Version Control Plan: I uploaded my project on Github. I will use the version control
                            tool according to best practices advised by professionals.

7. Module List: I will not be using any external modules/hardware/technologies.

