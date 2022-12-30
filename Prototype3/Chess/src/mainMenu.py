import pygame
import button
import whiteMain, easyWhiteMain
import blackMain, easyBlackMain
import Main
import mainNoUndo

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = True
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
startImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Picture1.png").convert_alpha()
optionsImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Options.png").convert_alpha()
quit_img = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Quit.png").convert_alpha()
back_img = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Back.png").convert_alpha()
progressImg=pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\PreviousGames.png").convert_alpha()

difficultyImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Difficulty.png").convert_alpha()
veryEasyImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\VeryEasy.png").convert_alpha()
easyImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Easy.png").convert_alpha()
mediumImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Medium.png").convert_alpha()
hardImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Hard.png").convert_alpha()
veryHardImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\VeryHard.png").convert_alpha()

opponentImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\opponent.png").convert_alpha()
computerImg =pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Computer.png").convert_alpha()
humanImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\human.png").convert_alpha()

colourImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\ChangeColour.png").convert_alpha()
whiteImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\White.png").convert_alpha()
blackImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Black.png").convert_alpha()

timerImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Timer.png").convert_alpha()
takebackImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Takebacks.png").convert_alpha()
enabledImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Enabled.png").convert_alpha()
disabledImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype3\Chess\images\Disabled.png").convert_alpha()

#create button instances
startButton = button.Button(300, 100, startImg, 1)
optionsButton = button.Button(300, 250, optionsImg, 1)
quit_button = button.Button(300, 375, quit_img, 1)
back_button = button.Button(300, 250, back_img, 1)
progressButton = button.Button(550,250,progressImg,1)

selectOpponentButton = button.Button(75,75, opponentImg,1)
computerButton =button.Button(75,75,computerImg,1)
humanButton = button.Button(300,75,humanImg,1)

changecolourButton = button.Button(300,75, colourImg,1)
whiteButton =button.Button(75,75, whiteImg,1)
blackButton =button.Button(300,75, blackImg,1)

difficultybutton = button.Button(75,250, difficultyImg,1)
veryEasyButton = button.Button(75,75,veryEasyImg,1)
EasyButton = button.Button(75,250,easyImg,1)
mediumButton = button.Button(300,75,mediumImg,1)
hardButton = button.Button(525,75,hardImg,1)
veryhardButton = button.Button(525,250,veryHardImg,1)

timerbutton = button.Button(525,75,timerImg,1)
takebackButton = button.Button(525,250,takebackImg,1)
enabledButton =button.Button(75,75,enabledImg,1)
disabledButton = button.Button(300,75,disabledImg,1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def main(game_paused, menu_state):

  #game_paused = True
  #menu_state = "main"

  #game loop
  run = True
  while run:

    screen.fill((52, 78, 91))

    if game_paused == True:
      #check menu state
      if menu_state == "main":

        #draw pause screen buttons
        if startButton.draw(screen):
          game_paused = False

          if opponent == "computer":
            if colour == "white":         
              if difficulty == "easy":
                easyWhiteMain.main()
              else:
                whiteMain.main()
            else:
              if difficulty == "easy":
                easyBlackMain.main()
              else:
                blackMain.main()
          else:
            if takebacks == True:
              mainNoUndo.main()
            else:
              Main.main()

        if optionsButton.draw(screen):
          menu_state = "options"
        if quit_button.draw(screen):
          run = False
        if progressButton.draw(screen):
          progressFile=open(r"progress.txt","r")
          progressFile.readlines()
          
      #check if the options menu is open
      if menu_state == "options":
        #draw the different options buttons
        if selectOpponentButton.draw(screen):
          menu_state = "opponent"

        if difficultybutton.draw(screen):
          menu_state = "difficulty"
        
        if changecolourButton.draw(screen):
          print("Change colour")
          menu_state = "colour"

        if timerbutton.draw(screen):
          print("Change timer Settings")
          menu_state = "timer"

        if takebackButton.draw(screen):
          print("change takeback settings")
          menu_state = "takeback"

        if back_button.draw(screen):
          menu_state = "main"

      elif menu_state == "colour":
        if whiteButton.draw(screen):
          colour = "white"

        if blackButton.draw(screen):
          colour = "black"

        if back_button.draw(screen):
          menu_state = "options"

      elif menu_state == "opponent":

        if computerButton.draw(screen):
          opponent = "computer"

        if humanButton.draw(screen):
          opponent = "human"

        if back_button.draw(screen):
          menu_state = "options"

      elif menu_state == "difficulty":
          if veryEasyButton.draw(screen):
            difficulty = "very easy"

          if EasyButton.draw(screen):
            difficulty = "easy"

          if mediumButton.draw(screen):
            difficulty = "medium"

          if hardButton.draw(screen):
            difficulty = "hard"
            
          if veryhardButton.draw(screen):
            difficulty = "very hard"

          if back_button.draw(screen):
            menu_state = "options"

      elif menu_state == "timer":
          if enabledButton.draw(screen):
            timer = True

          elif disabledButton.draw(screen):
            timer = False
            
          elif back_button.draw(screen):
            menu_state = "options"

      elif menu_state == "takeback":
          if enabledButton.draw(screen):
            takebacks = True

          elif disabledButton.draw(screen):
            takebacks = False

          elif back_button.draw(screen):
              menu_state = "options"

    else:
      draw_text("Press SPACE to continue", font, TEXT_COL, 160, 250)

    #event handler
    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_paused = True
      if event.type == pygame.QUIT:
        run = False
    
    pygame.display.update()

  pygame.quit()

if __name__ == "__main__":
  main(game_paused, menu_state)
  game_paused = False