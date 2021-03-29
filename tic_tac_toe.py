'''
Tic Tac Toe Game
Made by Steven Meyer
'''
import time
import pygame
pygame.init()


'''
Setting up some basic constants that will be used throughout program
'''
WIDTH = 600
HEIGHT = 800
TILE_SIZE = WIDTH/3
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("Comic Sans MS", 72)
winner1_text = font.render('Player 1 Wins!', False, (255, 255, 255))
winner2_text = font.render('Player 2 Wins!', False, (255, 255, 255))
tie_text = font.render('It is a tie!', False, (255, 255, 255))


BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREY = [192, 192, 192]
RED = [255, 0, 0]
player_turn = 1

running = True

# -1 is unfilled, 0 is O, 1 is X
board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

tiles = []  # top left corners of every square

'''
Initializing tiles array to contain the top left corner positions of each square
'''
for i in range(3):
    for j in range(3):
        tiles.append([j * TILE_SIZE, i * TILE_SIZE])

# print(tiles)


def draw_x(x, y, s):
    pygame.draw.line(screen, BLACK, [x, y], [x + s, y + s], 2)
    pygame.draw.line(screen, BLACK, [x, y + s], [x + s, y], 2)


def draw_buttons():
    padding = 2
    pygame.draw.rect(screen, RED, (0+padding, TILE_SIZE*3+ (2*padding), 80, 40))


def draw_o(x, y, size):
    pygame.draw.circle(screen, BLACK, [int(x + (TILE_SIZE/2)), int(y + (TILE_SIZE/2))], int(TILE_SIZE/2), 2)


def draw_lines():
    for i in range(1, 4):
        pygame.draw.line(screen, BLACK, [i * TILE_SIZE, 0], [i * TILE_SIZE, TILE_SIZE*3], 2)
        pygame.draw.line(screen, BLACK, [0, i * TILE_SIZE], [TILE_SIZE*3, i * TILE_SIZE], 2)


def check_win():
    if board[0] == board[1] == board[2] != -1:
        return board[0]
    if board[3] == board[4] == board[5] != -1:
        return board[3]
    if board[6] == board[7] == board[8] != -1:
        return board[6]
    if board[0] == board[4] == board[8] != -1:
        return board[0]
    if board[2] == board[4] == board[6] != -1:
        return board[2]
    if board[0] == board[3] == board[6] != -1:
        return board[0]
    if board[1] == board[4] == board[7] != -1:
        return board[1]
    if board[2] == board[5] == board[8] != 1:
        return board[2]
    return -1


def check_full():
    for x in board:
        if x == -1:
            return False
    return True


def reset():
    for n in range(9):
        board[n] = -1

    global player_turn
    player_turn = 1


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # gets position of mouse click
            pos = pygame.mouse.get_pos()
            if (0, TILE_SIZE*3) <= pos <= (80, TILE_SIZE*3 + 40): # reset button coords
                reset()
            counter = 0
            for coord in tiles: # check which square mouse was clicked in
                if coord[0] < pos[0] < coord[0] + TILE_SIZE and coord[1] < pos[1] < coord[1] + TILE_SIZE:
                    if player_turn == 1 and board[counter] == -1: # if player_turn = 1 set that square to be a 1("X")
                        board[counter] = 1
                        player_turn = 0
                    elif player_turn == 0 and board[counter] == -1: # if player_turn == 0 set that square to be a 0("O")
                        board[counter] = 0
                        player_turn = 1
                counter += 1

    screen.fill(GREY) # background
    draw_lines() # draw game lines
    draw_buttons() # draw button(s)
    for i in range(9):
        if board[i] == 1:
            draw_x(tiles[i][0], tiles[i][1], TILE_SIZE)
        elif board[i] == 0:
            draw_o(tiles[i][0], tiles[i][1], TILE_SIZE)

    winner = check_win()

    if winner == 1:
        screen.blit(winner1_text, (0, (HEIGHT/2) - (winner1_text.get_rect().height/2)))
        pygame.display.flip()
        time.sleep(3)
        reset()
        pygame.event.clear()

    elif winner == 0:
        screen.blit(winner2_text, (0, (HEIGHT / 2) - (winner2_text.get_rect().height / 2)))
        pygame.display.flip()
        time.sleep(3)
        reset()
        pygame.event.clear()

    elif check_full():
        screen.blit(tie_text, (0, (HEIGHT / 2) - (winner2_text.get_rect().height / 2)))
        pygame.display.flip()
        time.sleep(3)
        reset()
        pygame.event.clear()

    pygame.display.flip()
