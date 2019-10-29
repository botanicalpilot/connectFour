class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def name(self):
        name = input("What is the players name? ")
        return player

    def color(self):
        color = input("What is the players color? ")
        return color

class Game:
    def __init__(self, row1 = [0,0,0,0,0,0], row2 = [0,0,0,0,0,0], row3 = [0,0,0,0,0,0], row4 = [0,0,0,0,0,0], row5 = [0,0,0,0,0,0], row6 = [0,0,0,0,0,0], row7 = [0,0,0,0,0,0]):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.row5 = row5
        self.row6 = row6
        self.row7 = row7

    def __repr__(self):

         return f'{self.row1[5]}|{self.row2[5]}|{self.row3[5]}|{self.row4[5]}|{self.row5[5]}|{self.row6[5]}|{self.row7[5]}\n{self.row1[4]}|{self.row2[4]}|{self.row3[4]}|{self.row4[4]}|{self.row5[4]}|{self.row6[4]}|{self.row7[4]}\n{self.row1[3]}|{self.row2[3]}|{self.row3[3]}|{self.row4[3]}|{self.row5[3]}|{self.row6[3]}|{self.row7[3]}\n{self.row1[2]}|{self.row2[2]}|{self.row3[2]}|{self.row4[2]}|{self.row5[2]}|{self.row6[2]}|{self.row7[2]}\n{self.row1[1]}|{self.row2[1]}|{self.row3[1]}|{self.row4[1]}|{self.row5[1]}|{self.row6[1]}|{self.row7[1]}\n{self.row1[0]}|{self.row2[0]}|{self.row3[0]}|{self.row4[0]}|{self.row5[0]}|{self.row6[0]}|{self.row7[0]}'



    #def board(self):
        
       

    


    #def getHeight(self):
        #find the number of 0 left in list of six to determine. 
    #def move(self):
        #pick a row to place color. Color is placed at the last availible 0

    #def calcWinner():

    #def isFull():

    #def gameOverCheck():

def main():
    theGame = Game()

    player1 = Player.name()
    player1Color = Player.color()

    player2 = Player.name()
    player2Color = Player.color()



yay = Game()
print(yay.__repr__())