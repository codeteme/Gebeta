class Model:
    def __init__(self):
        self.currentPlayer = 0
        self.valueSmallBucket = [4] * 12
        self.valueLargeBucket = [0] * 2

    def getCurrentPlayer(self):
        return self.currentPlayer

    def switchPlayers(self):
        self.currentPlayer = (self.getCurrentPlayer() + 1) % 2

    def marbleImage(self):
        # Todo: Put the images in this dictionary
        marbleCount = dict()

    # # Create a method that randomly generates and holds the values of each small bucket.
    # # The string value of the elements in the store will be
    # # mapped to the text attribute of corresponding small buttons.
    #
    # def setInitialSmallBuckets(self):
    #     self.valueSmallBucket = [random.randint(0, 6) for i in range(12)]
    #     return self.valueSmallBucket

    # This method returns the values held by each small bucket
    def getSmallBuckets(self):
        return self.valueSmallBucket

    def setSmallBucket(self, position, amount):
        self.valueSmallBucket[position] = amount

    def addSmallBucket(self, position, amountAdd):
        self.valueSmallBucket[position] += amountAdd

    # This method returns the values held by each large bucket
    def getLargeBuckets(self):
        return self.valueLargeBucket

    def addLargeBucket(self, position, amountAdd):
        self.valueLargeBucket[position] += amountAdd

    # If either player fills up the large bucket first, they win.
    def isGameOver(self):
        return self.getLargeBuckets()[0] == 10 or self.getLargeBuckets()[1] == 10

    # This function takes in the position of the button clicked on and
    # returns true if each player clicks on a non-empty small bucket, and
    # the bucket selected is located on the player's side
    def isValidMove(self, x):
        if self.getCurrentPlayer() == 0:
            # Player 0 can only click on first six non-empty buckets
            return x >= 0 and x <= 5 and self.getSmallBuckets()[x] > 0
        elif self.getCurrentPlayer() == 1:
            # Player 1 can only click on last six non-empty buckets
            return x >= 6 and x <= 11 and self.getSmallBuckets()[x] > 0

    def makeMove(self, x):
        marbles = self.getSmallBuckets()[x]
        # The clicked bucket will be empty.
        self.setSmallBucket(x, 0)

        # If player 0 is selected marbles move counter-clockwise
        if self.getCurrentPlayer() == 0:
            for i in range(marbles):
                if x == 11:
                    x = 0
                self.addSmallBucket(x + 1, 1)
                x += 1
            print('after: ', self.getSmallBuckets())
            self.switchPlayers()

        # If player 1 is selected marbles move clockwise
        elif self.getCurrentPlayer() == 1:
            for i in range(marbles):
                print('i: ', i)
                if x >= 6 and x <= 10:
                    print('Button Pressed: ', x)
                    self.addSmallBucket(x + 1, 1)
                    x += 1
                # After bucket 11, marble move to right big bucket
                # Todo: Add marble to right big bucket
                if x == 11:
                    print('Button Pressed: ', x)

                    print('Button 11')
                    # marblesLeft = marbles-i
                    # if marblesLeft > 0:
                    self.addLargeBucket(1, 1)
                    i += 1
                    x = 4
                if x <= 4 and x >= 1:
                    print('Button Pressed: ', x)

                    print('Button between 4 and 1')
                    self.addSmallBucket(x - 1, 1)
                    x -= 1
                if x == 0:
                    print('Button Pressed: ', x)

                    print('Button 0')
                    self.addLargeBucket(0, 1)
                    x = 6
            print('after: ', self.getSmallBuckets())
            self.switchPlayers()

    def reset(self):
        return None
