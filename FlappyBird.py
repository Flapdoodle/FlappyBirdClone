import pygame
import random


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
song = 'C:/Users/Austin Abate/Downloads/Gamesongs/Track1.wav'
pygame.mixer.music.load(song)
pygame.mixer.music.play(-1)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
DisplayWidth = 600
DisplayHeight = 400
pygame.display.set_caption('Austins Game')
screen = pygame.display.set_mode((DisplayWidth, DisplayHeight))
background = pygame.Surface(screen.get_size())
background.fill((white))
background = background.convert()
screen.blit(background, (0,0))
FPS = 60
clock = pygame.time.Clock()
MAKERECTS = pygame.USEREVENT + 1
pygame.time.set_timer(MAKERECTS, 1990)

    
def mainloop():
    mainloop = True
    global score
    score = 0
    global xStart, yStart, blockWidth, blockHeight, RectHeight1
    xStart = DisplayWidth/2
    yStart = DisplayHeight/2
    blockWidth = 20
    blockHeight = 20
    RectXStart = DisplayWidth
    RectYStart1 = 0
    RectWidth = blockWidth

    RectHeight1 = 200
    RectYStart2 = 250
    RectHeight2 = DisplayHeight
    global enemy1, enemy2, startMOVERECT
    startMOVERECT = False
    NewRectValue = False
    while mainloop == True:
        keys = pygame.key.get_pressed()
        screen.fill(white)
        player = pygame.draw.rect(screen, black, ([xStart, yStart, blockWidth, blockHeight]))
        enemy1 = pygame.Rect([RectXStart, RectYStart1, RectWidth, RectHeight1])
        enemy2 = pygame.Rect([RectXStart, RectYStart2, RectWidth, RectHeight2])
        pygame.draw.rect(screen, red, (enemy1))
        pygame.draw.rect(screen, red, (enemy2))
        if startMOVERECT == True:
            RectXStart = RectXStart - 5

        if NewRectValue == True:
            RectHeight1 = random.randint(1, DisplayHeight - blockHeight * 2)
            RectYStart2 = DisplayHeight - (DisplayHeight - RectHeight1) + (blockHeight * 5)
            RectHeight2 = DisplayHeight - RectHeight1
            NewRectValue = False
            
        if player.colliderect(enemy1):
            pygame.quit()
        if player.colliderect(enemy2):
            pygame.quit()
        if RectXStart < 0:
            RectXStart = RectXStart + DisplayWidth
        if keys[pygame.K_UP]:  
            yStart = yStart - 12
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
                                      
            if event.type == MAKERECTS:
                startMOVERECT = True
                NewRectValue = True
                score = score + 1
                pygame.display.flip()
                
                
        text = "Score: {1:.1f}".format(clock.get_fps(), score)
        pygame.display.set_caption(text)        
        yStart = yStart + 6
        clock.tick(FPS)
        pygame.display.flip()

        if yStart > DisplayHeight - blockHeight:
            break
        if yStart < 0:
            break
                    
        

mainloop()
pygame.quit()
