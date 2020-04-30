import pygame
import Player
pygame.init()

BOARD_LENGTH = 1000
BOARD_HEIGHT = 500
SPRITE_WIDTH = 32
win = pygame.display.set_mode((BOARD_LENGTH,BOARD_HEIGHT))
pygame.display.set_caption("Jump")

CR = [pygame.image.load('CR1.png'), pygame.image.load('CR2.png'), pygame.image.load('CR3.png')]
CL = [pygame.image.load('CL1.png'), pygame.image.load('CL2.png'), pygame.image.load('CL3.png')]
SR = [pygame.image.load('SR1.png'), pygame.image.load('SR2.png'), pygame.image.load('SR3.png')]
SL = [pygame.image.load('SL1.png'), pygame.image.load('SL2.png'), pygame.image.load('SL3.png')]

FI = [pygame.image.load('FI1.png'), pygame.image.load('FI2.png'), pygame.image.load('FI3.png'), pygame.image.load('FI4.png'), pygame.image.load('FI5.png'), pygame.image.load('FI6.png'), pygame.image.load('FI7.png'), pygame.image.load('FI9.png'), pygame.image.load('FI8.png')]

TEXTURE_1 = [pygame.image.load('T1_1.png'), pygame.image.load('T1_2.png'), pygame.image.load('T1_3.png')]
BG = pygame.image.load('BG.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,w,h,s,p,j,e):
        self.x = x #x coordinate of picture
        self.y = y #y coordinate of picture
        self.width = w #width
        self.height = h #height
        self.right = True
        self.moving = False
        self.speed = s #speed of the character
        self.sprite = p # the sprite
        self.walk = 0 #counter for walking image
        self.jump = j #jump height of character
        self.isJump = False
        self.energy = e #energy of character

    
    def draw(self,win):
        if self.walk + 1 >= 9:
            self.walk = 0
        win.blit(self.sprite[self.right][self.walk//3], (self.x, self.y))
        if self.moving:
            self.walk += 1


EXPLOSION_WIDTH = 8
EXPLOSION_FRAMES = 9
class explosion(object):
    def __init__(self):
        self.x = -100
        self.y = -100
        self.timer = EXPLOSION_FRAMES
        self.i = 0

    def start(self, loc_x, loc_y):
        self.x = loc_x - EXPLOSION_WIDTH/2
        self.y = loc_y - EXPLOSION_WIDTH/2
        self.timer = 0

    def draw(self, win):      
        if self.timer < EXPLOSION_FRAMES:
            if self.i < 5:
                win.blit(FI[self.timer], (self.x, self.y))
                win.blit(FI[self.timer], (self.x - 20, self.y-20))
                win.blit(FI[self.timer], (self.x + 20, self.y-20))
                win.blit(FI[self.timer], (self.x - 10, self.y-10))
                win.blit(FI[self.timer], (self.x + 10, self.y-10))
                self.i += 1
            else:
                self.timer += 1
                self.i = 0
            self.y -= 20 * 0.5 * -1




TYRA = player(300, 490-SPRITE_WIDTH, 1, 1, 3, [SL,SR], 2, 3)
SAM = player(100, 490-SPRITE_WIDTH, 1, 1, 4, [CL,CR], 6, 3)
Explosion = explosion()



def redrawgamewindow():
    win.blit(BG, (0, 0))
    win.blit(BG, (BOARD_LENGTH/2, 0))
    pygame.draw.rect(win, (89,89,56), (0, 490, BOARD_LENGTH, 20), 20)
    
    SAM.draw(win)
    TYRA.draw(win)
    Explosion.draw(win)
    pygame.display.update()
    


run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and TYRA.x > 0:
        TYRA.x -= TYRA.speed
        TYRA.right = False
        TYRA.moving = True
    if keys[pygame.K_RIGHT] and TYRA.x < BOARD_LENGTH - SPRITE_WIDTH:
        TYRA.x += TYRA.speed
        TYRA.right = True
        TYRA.moving = True
    if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
        TYRA.moving = False
        TYRA.walk = 0
    if not(TYRA.isJump):
        if keys[pygame.K_UP]:
            TYRA.isJump = True
            TYRA.walkCount = 0
    else:
        if TYRA.jump >= -2:
            neg = 1
            if TYRA.jump < 0:
                neg = -1
            TYRA.y -= (TYRA.jump ** 2) * 0.5 * neg
            TYRA.jump -= .125
        else:
            TYRA.isJump = False
            TYRA.jump = 2
    
    if pygame.mouse.get_pressed()[0]:
        Mouse_x, Mouse_y= pygame.mouse.get_pos()
        print(Mouse_x)
        print(Mouse_y)
        print('Coordinate')
        Explosion.start(Mouse_x,Mouse_y)

    if keys[pygame.K_a] and SAM.x > 0:
        SAM.x -= SAM.speed
        SAM.right = False
        SAM.moving = True
    if keys[pygame.K_d] and SAM.x < BOARD_LENGTH - SPRITE_WIDTH:
        SAM.x += SAM.speed
        SAM.right = True
        SAM.moving = True
    if not (keys[pygame.K_d] or keys[pygame.K_a]):
        SAM.moving = False
        SAM.walk = 0    
    if not(SAM.isJump):
        if keys[pygame.K_w]:
            SAM.isJump = True
            SAM.walkCount = 0
    else:
        if SAM.jump >= -6:
            neg = 1
            if SAM.jump < 0:
                neg = -1
            SAM.y -= (SAM.jump ** 2) * 0.4 * neg
            SAM.jump -= 1
        else:
            SAM.isJump = False
            SAM.jump = 6

    redrawgamewindow()

pygame.quit()
