import tkinter as tk
from tkinter import messagebox
from model import *

# The game should have the following:
# * Title of the game
# * Label that indicates the current player
# * Label that indicates which row belongs to which player. (Player 1 and Player 2)
# * Button that reads 'Click here for instruction'.
# * Button for the small holes will be buttons and the text will be the marbles in that hole.
# * Labels of slightly large sizes for the two big buckets.
# * Button that allows for restart.

class View:
    def __init__(self, window, model):
        self.model = model

        # Create a new frame to store the active player
        self.frmStatus = tk.Frame(window, borderwidth=2, relief='ridge', width=50, height=50)
        self.lblCurrentPlayer = tk.Label(master=self.frmStatus,
                                         text=f'Current Player: {self.model.getCurrentPlayer()}')
        self.frmStatus.grid(row=0, column=0, columnspan=3, rowspan=2)
        self.lblCurrentPlayer.grid(sticky='w')

        # Create a new frame to store all the small and big buckets, and
        # indicate which row belongs to which player
        self.frmBuckets = tk.Frame(window, borderwidth=30, relief='ridge', width=300, height=300)
        self.lblRowPlayer1 = tk.Label(master=self.frmBuckets, text=f'Player 1')
        self.lblRowPlayer1.grid(columnspan=30)
        # I copied it from here but I certainly tweaked it a little bit:
        # https://stackoverflow.com/questions/4236182/generate-tkinter-buttons-dynamically
        self.smallBuckets = []
        self.largeBuckets = []
        for i in range(12):
            if i == 0:
                leftLargeBucket = tk.Label(self.frmBuckets, text=self.model.getLargeBuckets()[0],
                                           width=5, height=10,
                                           borderwidth=2, relief="groove")
                leftLargeBucket.grid(row=3, column=1, rowspan=5)
                self.largeBuckets.append(leftLargeBucket)
            if i == 7:
                rightLargeBucket = tk.Label(self.frmBuckets, text=self.model.getLargeBuckets()[1],
                                      width=5, height=10,
                                      borderwidth=2, relief="groove")
                self.largeBuckets.append(leftLargeBucket)
                rightLargeBucket.grid(row=3, column=15, rowspan=5)
                # rightLargeBucket.grid(row=i // 2, column=i % 6)
            newSmallBucket = tk.Button(self.frmBuckets, text=self.model.getSmallBuckets()[i],
                                       width=10, height=5,
                                       command=lambda x=i: self.bucketPressed(x))
            self.smallBuckets.append(newSmallBucket)
            newSmallBucket.grid(row=(i // 6) + 6, column=(i % 6) + 6)
        self.lblRowPlayer2 = tk.Label(master=self.frmBuckets, text=f'Player 2')
        self.lblRowPlayer2.grid(columnspan=30)

        self.frmBuckets.grid(row=3, column=0, columnspan=3, rowspan=2)

        # Create a new frame to hold the reset button
        self.frmRestart = tk.Frame(window)
        btnReset = tk.Button(master=self.frmRestart, text='Restart',
                             command=lambda: self.reset())
        self.frmRestart.grid(row=10, column=0, columnspan=3, rowspan=2)
        btnReset.grid(columnspan=30)

    # The underlying logic for this function is inspired by Professor's tic-tac-toe GUI.py
    def bucketPressed(self, x):
        if not self.model.isGameOver():
            if self.model.isValidMove(x):
                self.lblCurrentPlayer['text'] = f'Current Player: {self.model.getCurrentPlayer()}'
                self.model.makeMove(x)
                for i in range(2):
                    self.largeBuckets[i]['text'] = str(self.model.getLargeBuckets()[i])
                # Modify the text attribute of the buckets to reflect the changes
                for i in range(12):
                    self.smallBuckets[i]['text'] = str(self.model.getSmallBuckets()[i])
                # Todo: Change the configuration of the image attribute
                # Todo: Switch Players if last marble lands in
                #       current player's big bucket
            else:
                print('Not a valid move')
        if self.model.isGameOver():
            tk.messagebox.showinfo('Result', 'You won')
        return None

    # Reset all the values of all the big and small buckets
    def reset(self):
        # Todo: Figure out the complexity of the calling or re-calling the model.
        #               Do I maybe need to call the controller?
        # self.model = model
        # todo: delete the old window
        newC = Controller()
        newC.run()


class Controller:
    def __init__(self):
        # Create the main windows to work on
        self.window = tk.Tk()
        self.model = Model()
        self.view = View(self.window, self.model)

    def run(self):
        self.window.title('Gebeta')
        # self.window.columnconfigure(0, minsize=250)
        # self.window.rowconfigure([0, 1], minsize=100)
        self.window.deiconify()  # Displays the window
        self.window.mainloop()


c = Controller()
c.run()
