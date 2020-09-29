import pygame
from sys import exit
import sudoku


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((450, 450))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
notefont = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for y in range(9):
    for x in range(9):
        board[y][x] = sudoku.boards[0][y][x]

buttons = [[None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None],
           [None, None, None, None, None, None, None, None, None]]


note = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def checkDone():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return False
    return True


def good(b, row, col):
    screen.fill((255, 255, 255))
    for y in range(3):
        for x in range(3):
            numX = 150*x
            numY = 150*y
            pygame.draw.rect(screen, (0, 0, 0), (numX, numY, 150, 150), 2)

    for y in range(9):
        for x in range(9):
            numX = 50*x
            numY = 50*y
            pygame.draw.rect(screen, (0, 0, 0), (numX, numY, 50, 50), 1)
            if b[y][x] == 0:
                textsurface = myfont.render('', True, (0, 0, 0))
                screen.blit(textsurface, (numX + 18, numY + 5))
            else:
                textsurface = myfont.render(str(b[y][x]), True, (0, 0, 0))
                screen.blit(textsurface, (numX + 18, numY + 5))

    pygame.draw.rect(screen, (0, 255, 0), (col*50, row*50, 50, 50), 3)
    pygame.display.update()
    currTime = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if pygame.time.get_ticks() - currTime >= 100:
            return


def bad(b, row, col):
    b[row][col] = 0
    screen.fill((255, 255, 255))
    for y in range(3):
        for x in range(3):
            numX = 150*x
            numY = 150*y
            pygame.draw.rect(screen, (0, 0, 0), (numX, numY, 150, 150), 2)

    for y in range(9):
        for x in range(9):
            numX = 50*x
            numY = 50*y
            pygame.draw.rect(screen, (0, 0, 0), (numX, numY, 50, 50), 1)
            if b[y][x] == 0:
                textsurface = myfont.render('', True, (0, 0, 0))
                screen.blit(textsurface, (numX + 18, numY + 5))
            else:
                textsurface = myfont.render(str(b[y][x]), True, (0, 0, 0))
                screen.blit(textsurface, (numX + 18, numY + 5))

    pygame.draw.rect(screen, (255, 0, 0), (col*50, row*50, 50, 50), 3)
    clock.tick(60)
    pygame.display.update()
    currTime = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if pygame.time.get_ticks() - currTime >= 100:
            return


def main():
    global board
    global note
    click = False
    running = True

    while running:

        screen.fill((255, 255, 255))
        for y in range(3):
            for x in range(3):
                numX = 150*x
                numY = 150*y
                pygame.draw.rect(screen, (0, 0, 0), (numX, numY, 150, 150), 2)

        for y in range(9):
            for x in range(9):
                numX = 50*x
                numY = 50*y
                buttons[y][x] = pygame.Rect(numX, numY, 50, 50)
                pygame.draw.rect(screen, (0, 0, 0), buttons[y][x], 1)
                if board[y][x] == 0:
                    if note[y][x] != 0:
                        textsurface = notefont.render(
                            str(note[y][x]), True, (211, 211, 211))
                        screen.blit(textsurface, (numX + 2, numY))
                    else:
                        textsurface = myfont.render('', True, (0, 0, 0))
                        screen.blit(textsurface, (numX + 18, numY + 5))
                else:
                    textsurface = myfont.render(
                        str(board[y][x]), True, (0, 0, 0))
                    screen.blit(textsurface, (numX + 18, numY + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mX, mY = pygame.mouse.get_pos()
                    if buttons[mY//50][mX//50].collidepoint((mX, mY)) and board[mY//50][mX//50] == 0:
                        click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sudoku.solve(sudoku.boards[0])
                    pygame.time.delay(2000)
                    running = False

                if click:

                    if event.key == pygame.K_RETURN:
                        if buttons[mY//50][mX//50].collidepoint((mX, mY)) and note[mY//50][mX//50] != 0 and sudoku.isValid(board, mY//50, mX//50, note[mY//50][mX//50]):
                            board[mY//50][mX//50] = note[mY//50][mX//50]
                            textsurface = myfont.render(
                                str(board[mY//50][mX//50]), True, (0, 0, 0))
                            screen.blit(textsurface, (mX//50 + 18, mY//50 + 5))
                    else:
                        if event.key == pygame.K_1:
                            note[mY//50][mX//50] = 1
                        elif event.key == pygame.K_2:
                            note[mY//50][mX//50] = 2
                        elif event.key == pygame.K_3:
                            note[mY//50][mX//50] = 3
                        elif event.key == pygame.K_4:
                            note[mY//50][mX//50] = 4
                        elif event.key == pygame.K_5:
                            note[mY//50][mX//50] = 5
                        elif event.key == pygame.K_6:
                            note[mY//50][mX//50] = 6
                        elif event.key == pygame.K_7:
                            note[mY//50][mX//50] = 7
                        elif event.key == pygame.K_8:
                            note[mY//50][mX//50] = 8
                        elif event.key == pygame.K_9:
                            note[mY//50][mX//50] = 9
                        textsurface = notefont.render(
                            str(note[mY//50][mX//50]), True, (211, 211, 211))
                        screen.blit(textsurface, (mX//50 + 1, mY//50 + 1))
                    click = False

        clock.tick(60)
        pygame.display.update()

        if checkDone():
            running = False
