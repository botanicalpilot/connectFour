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

         return f'{self.row1[0]}|{self.row2[0]}|{self.row3[0]}|{self.row4[0]}|{self.row5[0]}|{self.row6[0]}|{self.row7[0]}\n{self.row1[1]}|{self.row2[1]}|{self.row3[1]}|{self.row4[1]}|{self.row5[1]}|{self.row6[1]}|{self.row7[1]}\n{self.row1[2]}|{self.row2[2]}|{self.row3[2]}|{self.row4[2]}|{self.row5[2]}|{self.row6[2]}|{self.row7[2]}\n{self.row1[3]}|{self.row2[3]}|{self.row3[3]}|{self.row4[3]}|{self.row5[3]}|{self.row6[3]}|{self.row7[3]}\n{self.row1[4]}|{self.row2[4]}|{self.row3[4]}|{self.row4[4]}|{self.row5[4]}|{self.row6[4]}|{self.row7[4]}\n{self.row1[5]}|{self.row2[5]}|{self.row3[5]}|{self.row4[5]}|{self.row5[5]}|{self.row6[5]}|{self.row7[5]}'



    def boardPlacement(self, rowChoice, playerColor):
        #row1
        if rowChoice == '1':
            if 0 not in self.row1:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '1':
                self.row1.append(playerColor)
                del self.row1[0]
                return self.row1
        
        #row2
        if rowChoice == '2':
            if 0 not in self.row2:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '2':
                self.row2.append(playerColor)
                del self.row2[0]
                return self.row2
        
        #row3
        if rowChoice == '3':
            if 0 not in self.row3:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '3':
                self.row3.append(playerColor)
                del self.row3[0]
                return self.row3
        
        #row4
        if rowChoice == '4':
            if 0 not in self.row4:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '4':
                self.row4.append(playerColor)
                del self.row4[0]
                return self.row4
        
        #row5
        if rowChoice == '5':
            if 0 not in self.row5:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '5':
                self.row5.append(playerColor)
                del self.row5[0]
                return self.row5
        
        #row6
        if rowChoice == '6':
            if 0 not in self.row6:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '6':
                self.row6.append(playerColor)
                del self.row6[0]
                return self.row6
        
        #row7
        if rowChoice == '7':
            if 0 not in self.row7:
                print('Row full, try a different row')
                #return True
            elif rowChoice == '7':
                self.row7.append(playerColor)
                del self.row7[0]
                return self.row7


       


        
       

    


    #def getHeight(self):
        #find the number of 0 left in list of six to determine. 
    #def move(self):
        #pick a row to place color. Color is placed at the last availible 0

    #def calcWinner():

    #def isFull():

    #def gameOverCheck():

def main():
    theGame = Game()

    player1 = 'Mark'
    player1Color = '*'

    player2 = 'Jon'
    player2Color = '#'

    
    while True:
        player1Placement = input(f'{player1}, which row, 1-7, do you want to place your color? ')
        player1Move = theGame.boardPlacement(player1Placement, player1Color)
        print(theGame.__repr__())

        player2Placement = input(f'{player2}, which row, 1-7, do you want to place your color? ')
        player2Move = theGame.boardPlacement(player2Placement, player2Color)
        print(theGame.__repr__())



main()
