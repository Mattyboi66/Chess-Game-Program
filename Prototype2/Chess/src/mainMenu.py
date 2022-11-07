import pygame
import button
import main

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
startImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Picture1.png").convert_alpha()
optionsImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Options.png").convert_alpha()
quit_img = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Quit.png").convert_alpha()
back_img = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Back.png").convert_alpha()
difficultyImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Difficulty.png").convert_alpha()
opponentImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\opponent.png").convert_alpha()
colourImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\ChangeColour.png").convert_alpha()
timerImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Timer.png").convert_alpha()
takebackImg = pygame.image.load(r"C:\Users\Anderson\Documents\matthew's homework\KS5\Computer Science\Programming project\Programme\Prototype2\Chess\images\Takebacks.png").convert_alpha()

#create button instances
startButton = button.Button(300, 100, startImg, 1)
optionsButton = button.Button(300, 250, optionsImg, 1)
quit_button = button.Button(300, 375, quit_img, 1)
back_button = button.Button(300, 250, back_img, 1)
selectOpponentButton = button.Button(75,75, opponentImg,1)
changecolourButton = button.Button(300,75, colourImg,1)
difficultybutton = button.Button(75,250, difficultyImg,1)
timerbutton = button.Button(525,75,timerImg,1)
takebackButton = button.Button(525,250,takebackImg,1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))


def options ():
  if menu_state == options:
      selectOpponentButton.draw(screen)
      changecolourButton.draw(screen)

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
        main.main()
      if optionsButton.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if selectOpponentButton.draw(screen):
        print("Change Opponent")

      if changecolourButton.draw(screen):
        print("Change Colour")

      if difficultybutton.draw(screen):
        print("Change Difficulty")

      if timerbutton.draw(screen):
        print("Change timer Settings")

      if takebackButton.draw(screen):
        print("change takeback settings")

      if back_button.draw(screen):
        menu_state = "main"
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

