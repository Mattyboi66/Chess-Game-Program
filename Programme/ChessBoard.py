from tkinter import *
from PIL import Image,ImageTk  
import math 
from ChessGame import Piece
from ChessAI import stockfish

class Board():
    
    def boardmain():

        root = Tk()
        root.title("Game")

        frame = Frame(root)
        frame.pack()

        canvas = Canvas(frame, bg="black", width=500, height=500)
        canvas.pack()

        background = PhotoImage(file=r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\board.png")
        canvas.create_image(250,250, image=background)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Pawn.png")
        img = image.resize((40,40))
        wPawn = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\BlackPawn.png")
        img = image.resize((65,65))
        bPawn = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\White Rook.png")
        img = image.resize((40,40))
        wRook = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Black Rook.png")
        img = image.resize((45,45))
        bRook = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\White Knight.png")
        img = image.resize((45,45))
        wKnight = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Black Knight.png")
        img = image.resize((35,35))
        bKnight = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\White Bishop.png")
        img = image.resize((45,45))
        wBishop = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Black Bishop.png")
        img = image.resize((40,40))
        bBishop = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\White Queen.png")
        img = image.resize((40,40))
        wQueen = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Black Queen.png")
        img = image.resize((40,40))
        bQueen = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\White King.png")
        img = image.resize((40,40))
        wKing = ImageTk.PhotoImage(img)

        image = Image.open(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Images\Black King.png")
        img = image.resize((40,40))
        bKing = ImageTk.PhotoImage(img)


        Matrix= [["bRook","bKnight","bBishop","bQueen","bKing","bBishop","bKnight","bRook"],
                ["bPawn","bPawn","bPawn","bPawn","bPawn","bPawn","bPawn","bPawn"],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["","","","","","","",""],
                ["wPawn","wPawn","wPawn","wPawn","wPawn","wPawn","wPawn","wPawn"],
                ["wRook","wKnight","wBishop","wQueen","wKing","wBishop","wKnight","wRook"]]

        line=len(Matrix)
        collumn=len(Matrix[0])
        def piecePosition():
            #black pawns 
            canvas.create_image(52,109,image=bPawn)
            canvas.create_image(107,109,image=bPawn)
            canvas.create_image(164,109,image=bPawn)
            canvas.create_image(220,109,image=bPawn)
            canvas.create_image(275,109,image=bPawn)
            canvas.create_image(332,109,image=bPawn)
            canvas.create_image(390,109,image=bPawn)
            canvas.create_image(443,109,image=bPawn)

            #black rooks 
            canvas.create_image(52,52,image=bRook)
            canvas.create_image(443,52,image=bRook)
            #black Knights
            canvas.create_image(109,52, image=bKnight)
            canvas.create_image(390,52, image=bKnight)

            #black bishops
            canvas.create_image(164,52,image=bBishop)
            canvas.create_image(332,52,image=bBishop)

            # black Queen
            canvas.create_image(220,52,image=bQueen)

            #black king 
            canvas.create_image(275,52,image=bKing)

            #white pawns 
            canvas.create_image(52,390,image=wPawn)
            canvas.create_image(107,390,image=wPawn)
            canvas.create_image(164,390,image=wPawn)
            canvas.create_image(220,390,image=wPawn)
            canvas.create_image(275,390,image=wPawn)
            canvas.create_image(332,390,image=wPawn)
            canvas.create_image(390,390,image=wPawn)
            canvas.create_image(443,390,image=wPawn)

            #white rooks 
            canvas.create_image(52,447,image=wRook)
            canvas.create_image(443,447,image=wRook)

            #white Knights
            canvas.create_image(107,447,image=wKnight)
            canvas.create_image(390,447,image=wKnight)

            #white bishops
            canvas.create_image(164,447,image=wBishop)
            canvas.create_image(332,447,image=wBishop)

            #white Queen 
            canvas.create_image(220,447,image=wQueen)

            #white King
            canvas.create_image(275,447,image=wKing)

        piecePosition()

        piece = None

        def getorigin(eventorigin):
            global Posx,Posy, piece
            Posx = eventorigin.x
            Posy = eventorigin.y
            Xcase = math.ceil((Posx / 62)) - 1
            Ycase = math.ceil((Posy / 62)) - 1
            
            if Matrix[Ycase][Xcase] != "":
        # select the piece
                piece = Matrix[Ycase][Xcase]
                preY = Ycase
                preX = Xcase
                print(piece)
            elif piece:
        # a piece is selected, so move the piece
                canvas.move(piece, Xcase*62.5+33, Ycase*62.5+33)
                
                Matrix[Ycase][Xcase] = piece
                Matrix[preY][preX] = ""
                piece = None  # deselect the piece 
                piecePosition()

        canvas.bind("<Button-1>", getorigin)
        root.title("Chess")
        root.iconbitmap()
        root.geometry("500x500")
        root.mainloop()

Board.boardmain()
