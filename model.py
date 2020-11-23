class Model:
    def __init__(self):
        self.currentPlayer = 0
        # All the small buckets are pre-populated with 4 marbles
        self.buckets = [4] * 14
        # The two large buckets don't have any marbles at first.
        self.buckets[6] = 0
        self.buckets[13] = 0

    def getCurrentPlayer(self):
        return self.currentPlayer

    def switchPlayers(self):
        self.currentPlayer = (self.getCurrentPlayer() + 1) % 2

    # def marbleImage(self):
    #     # Todo: Put the images in this dictionary
    #     marbleCount = dict()

    def setBucketValue(self, position, amount):
        self.buckets[position] = amount

    def addBucketValue(self, position, amountAdd):
        self.buckets[position] += amountAdd

    # This method return score of Player 0
    def getLeftLargeBucket(self):
        return self.buckets[6]

    # This method return score of Player 1
    def getRightLargeBucket(self):
        return self.buckets[13]

    # This method returns the values held by all small buckets
    def getAllBuckets(self):
        return self.buckets

    # If either player fills up the large bucket first, they win.
    def isGameOver(self):
        return self.getLeftLargeBucket() == 10 or self.getRightLargeBucket() == 10

    # This method checks only non-empty bucket is clickable
    # This method also checks player click on buckets located on their side
    # This method also checks player does not click on either of big buckets
    def isValidMove(self, x):
        if x == 6 or x == 13:
            return False
        if self.getCurrentPlayer() == 0:
            # Player 0 can only click on first six non-empty buckets
            return x >= 0 and x <= 5 and self.getAllBuckets()[x] > 0
        elif self.getCurrentPlayer() == 1:
            # Player 1 can only click on last six non-empty buckets
            return x >= 7 and x <= 12 and self.getAllBuckets()[x] > 0

    def makeMove(self, x):
        marbles = self.getAllBuckets()[x]
        self.setBucketValue(x, 0)
        j = 1
        print(self.getAllBuckets())
        while marbles > 0:
            if not (self.getCurrentPlayer() == 0 and x + j == 13):
                self.addBucketValue((x + j)%14, 1)
                marbles -= 1
            j += 1
        self.switchPlayers()