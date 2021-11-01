import pygame
import random
import math
import vlc

# installize the pygame
pygame.init()

# creat the screen
screen = pygame.display.set_mode((800, 500))

# sound
bc = vlc.MediaPlayer("back.webm")
bc.play()
dc = vlc.MediaPlayer("no.mp3")

# set title and icon
pygame.display.set_caption("sun")
icon = pygame.image.load('sun.png')
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load('chick.png')
x = 400
y = 200

x1 = 0
y1 = 0
# egg
egg_state = "off"
egg_img = pygame.image.load('egg.png')
egx = 0
egy = 0

# enimy
enimy_img = pygame.image.load('knife.png')
ex = random.randint(0, 740)
ey = random.randint(10, 440)

ex1 = 0.1
ey1 = 0.1

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# game over
g_font = pygame.font.Font('freesansbold.ttf', 80)

# life
life = "live"


def show_score():
    scr = font.render("Score:" + str(score), True, (110, 0, 255))
    screen.blit(scr, (0, 0))


def g_o():
    go = g_font.render("Game Over", True, (255, 255, 255))
    screen.blit(go, (200, 210))


def player():
    screen.blit(player_img, (x, y))
    screen.blit(enimy_img, (ex, ey))


def egg(egx, egy):
    global egg_state
    egg_state = "one"

    screen.blit(egg_img, (egx, egy))


def col(ex, ey, egx, egy):
    d = math.sqrt(math.pow(ex - egx, 2) + math.pow(ey - egy, 2))
    if d < 25:
        return True
    else:
        return False


def death(ex, ey, x, y):
    global life
    d1 = math.sqrt(math.pow(ex - x, 2) + math.pow(ey - y, 2))
    if d1 < 40:
        life = "die"
        bc.stop()
        dc.play()
        g_o()


# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # keystroke check
        if event.type == pygame.KEYDOWN:
            if life == "live":
                if event.key == pygame.K_LEFT:
                    x1 = - 0.5
                    print("left")
                if event.key == pygame.K_RIGHT:
                    x1 = 0.5
                    print("rigt")
                if event.key == pygame.K_UP:
                    y1 = - 0.5
                    print("up")
                if event.key == pygame.K_DOWN:
                    y1 = 0.5
                    print("down")
                if event.key == pygame.K_SPACE:
                    egx = x + 25
                    egy = y + 65
                    egg(egx, egy)
                    yes = vlc.MediaPlayer("yes.mp3")
                    yes.play()
                    print("space")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x1 = 0
                y1 = 0
                print("realsed")

    x = x1 + x
    y = y1 + y

    if life == "live":
        ex = ex + ex1
        ey = ey + ey1

    # player boundry
    if x < 0:
        x = 1
    elif x > 740:
        x = 740
    if y < 0:
        y = 1
    elif y > 440:
        y = 440

    spd = random.randint(1, 50)

    # enimy movement
    if ex < 0:
        ex1 = 5 / spd
    elif ex > 740:
        ex1 = -5 / spd

    if ey < 1:
        ey1 = 5 / spd
    elif ey > 440:
        ey1 = -5 / spd

    screen.fill((55, 20, 40))
    if egg_state == "one":
        egg(egx, egy)

    coll = col(ex, ey, egx, egy)
    if coll:
        score = score + 1
        egg_state = "off"
        print(score)

    death(ex, ey, x, y)

    show_score()
    player()

    pygame.display.update()
