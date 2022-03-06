from random import *
import pygame

pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
myFont = pygame.font.SysFont("arial", 30, True, False)
Font = pygame.font.SysFont("arial", 70, True, False)
a = []

def a_reset():
    global a
    a = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0],
    ]

class player:
    def __init__(self, name, color=0):
        self.name = name
        self.color = color

    def width(self, b):
        for i in range(len(b)):
            for j in range(len(b[i])-4):
                if b[i][j] == b[i][j+1] == b[i][j+2] == b[i][j+3] == b[i][j+4] == self.color:
                    return True
    def height(self, b):
        for i in range(len(b[0])):
            for j in range(len(b)-4):
                if b[j][i] == b[j+1][i] == b[j+2][i] == b[j+3][i] == b[j+4][i] == self.color:
                    return True
    def diagonal(self, b):
        for i in range(len(b)-4):
            for j in range(len(b[i])-4):
                if b[i][j] == b[i+1][j+1] == b[i+2][j+2] == b[i+3][j+3] == b[i+4][j+4] == self.color:
                    return True

    def check(self, b):
        w = self.width(b)
        h = self.height(b)
        d = self.diagonal(b)
        if w or h or d:
            return True

a_reset()

def design():
    screen.fill((206, 103, 0))
    for i in range(1, len(a)+1):
        pygame.draw.rect(screen, (0, 0, 0), (50, 50*i, 900, 2))
    for i in range(1, len(a[0])+1):
        pygame.draw.rect(screen, (0, 0, 0), (50*i, 50, 2, 900))

def go_stone():
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                pygame.draw.circle(screen, (0, 0, 0), (50+50*j, 50+50*i), 20)
            elif a[i][j] == 2:
                pygame.draw.circle(screen, (255, 255, 255), (50+50*j, 50+50*i), 20)

def font_player(turn):
    p1_t = myFont.render("player1 turn (Black)", True, (0, 0, 0))
    p2_t = myFont.render("player2 turn (White)", True, (0, 0, 0))

    pygame.draw.rect(screen, (206, 103, 0), (0, 0, 500, 40))
    if turn == 0:
        screen.blit(p1_t, (0, 0))
    elif turn == 1:
        screen.blit(p2_t, (0, 0))

def win(p):
    run = True
    fa = Font.render("push the space", True, (255, 255, 0))
    fb = Font.render("game start", True, (255, 255, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
                if event.key == pygame.K_ESCAPE:
                    run = False
        win_t = Font.render("player"+p.name+" win", True, (50, 0, 255))
        screen.blit(fa, (245, 500))
        screen.blit(fb, (320, 570))
        screen.blit(win_t, (290, 400))
        pygame.display.update()
    main()

def game():
    a_reset()
    p1 = player('1', 1)
    p2 = player('2', 2)

    u = 1
    m = False
    x1, y1 = 0, 0
    pre = [0, 0]
    w = 0
    turn = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_LCTRL:
                    u = 5            
                if event.key == pygame.K_RIGHT:
                    if (u == 1 and pre[0]+1 <= 18) or (u == 5 and pre[0]+5 <= 18):
                        pre[0] += 1*u
                        m = False
                if event.key == pygame.K_LEFT:
                    if (u == 1 and pre[0]-1 >= 0) or (u == 5 and pre[0]-5 >= 0):
                        pre[0] -= 1*u
                        m = False
                if event.key == pygame.K_UP:
                    if (u == 1 and pre[1]-1 >= 0) or (u == 5 and pre[1]-5 >= 0):
                        pre[1] -= 1*u
                        m = False   
                if event.key == pygame.K_DOWN:
                    if (u == 1 and pre[1]+1 <= 18) or (u == 5 and pre[1]+5 <= 18):
                        pre[1] += 1*u
                        m = False
                if event.key == pygame.K_SPACE:
                    if a[pre[1]][pre[0]] == 0:
                        if turn == 0:
                            a[pre[1]][pre[0]] = 1
                            turn = 1
                        elif turn == 1:
                            a[pre[1]][pre[0]] = 2
                            turn = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL:
                    u = 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if x < 25 or x > 975 or y < 25 or y > 975:
                        continue
                    x = (x-25)//50
                    y = (y-25)//50
                    if a[y][x] != 0:
                        continue
                    if turn == 0:
                        a[y][x] = 1
                        turn = 1
                        run = True
                    elif turn == 1:
                        a[y][x] = 2
                        turn = 0
                        run = True

        design()
        go_stone()

        x, y = pygame.mouse.get_pos()

        if x != x1 and y != y1:
            m = True
        if m:
            if turn == 0:
                for i in range(1, 20):
                    pygame.draw.circle(screen, (40-i*2, 40-i*2, 40-i*2), (x, y), 20-i)
            elif turn == 1:
                for i in range(1, 20):
                    pygame.draw.circle(screen, (205+i*2.5, 205+i*2.5, 205+i*2.5), (x, y), 20-i)
        else:
            if turn == 0:
                for i in range(1, 20):
                    pygame.draw.circle(screen, (40-i*2, 40-i*2, 40-i*2), (50+pre[0]*50, 50+pre[1]*50), 21-i)
            elif turn == 1:
                for i in range(1, 20):
                    pygame.draw.circle(screen, (205+i*2.5, 205+i*2.5, 205+i*2.5), (50+pre[0]*50, 50+pre[1]*50), 20-i)
        x1, y1 = x, y

        font_player(turn)

        if p1.check(a):
            w = 1
            run = False
        if p2.check(a):
            w = 2
            run = False

        pygame.display.update()

    if w == 1:
        win(p1)
    elif w == 2:
        win(p2)

def main():
    design()
    fa = Font.render("push the space", True, (255, 255, 0))
    fb = Font.render("game start", True, (255, 255, 0))

    c = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    c = True
                    run = False

        screen.blit(fa, (245, 400))
        screen.blit(fb, (320, 470))

        pygame.display.update()
    if c:
        game()

main()
