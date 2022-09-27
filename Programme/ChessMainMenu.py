from tkinter import *
from ChessAI import stockfish
from ChessBoard import Board

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=140, y=325)

        startButton = Button(self, text = "Start Game", command=Board.boardmain)
        startButton.place(x=135,y=300)

        selectColour = Button(self,text= "Select Colour", command=self.selectColour)
        selectColour.place (x=250,y=75)

        selectOpponent = Button(self,text= "Select Opponent", command=self.selectOpponent)
        selectOpponent.place (x=135,y=75)

        selectDifficulty = Button(self, text= "Select Difficulty", command=self.selectDifficulty)
        selectDifficulty.place (x=135,y=150)

    def clickStartButton(self):
        print("Start Game")
        Board.boardmain()
        

    def selectColour(self):
        print("Select Colour")
        WhiteColour = Button(self, text= "White", command=self.WhiteColour)
        WhiteColour.place (x=250,y=100)

        BlackColour = Button(self, text= "Black", command=self.BlackColour)
        BlackColour.place (x=250,y=125)

    def WhiteColour(self):
        print("White")

    def BlackColour(self):
        print("Black")

    def selectDifficulty(self):
        VeryEasyDifficulty = Button(self, text= "Very Easy", command=self.VeryEasy)
        VeryEasyDifficulty.place (x=135,y=175)

        EasyDifficulty = Button(self, text= "Easy", command=self.Easy)
        EasyDifficulty.place (x=135,y=200)

        MediumDifficulty = Button(self, text= "Medium", command=self.Medium)
        MediumDifficulty.place (x=135,y=225)

        HardDifficulty = Button(self, text= "Hard", command=self.Hard)
        HardDifficulty.place (x=135,y=250)

        VeryHardDifficulty = Button(self, text= "Very Hard", command=self.VeryHard)
        VeryHardDifficulty.place (x=135,y=275)
        print ("Select Difficulty")
    
    def selectOpponent(self):
        print("Select Opponent")
        AIOpponent = Button(self, text= "Computer", command=self.Computer)
        AIOpponent.place (x=135,y=100)

        FriendOpponent = Button(self, text= "Friend", command=self.Friend)
        FriendOpponent.place (x=135,y=125)
    
    def Computer(self):
        print("Against computer")
    
    def Friend(self):
        print("Against Friend")
    
    def VeryEasy(self):
        stockfish.stockfish.set_elo_rating(300)

    def Easy(self):
        stockfish.stockfish.set_elo_rating(500)
    
    def Medium(self):
        stockfish.stockfish.set_elo_rating(1000)

    def Hard(self):
        stockfish.stockfish.set_elo_rating(1500)
    
    def VeryHard(self):
        stockfish.stockfish.set_elo_rating(1500)
        

    def clickExitButton(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("500x500")
root.mainloop()
