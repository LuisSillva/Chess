'''
Main driver file. Responsável pelas interaçõs com o Usuário e mostrar o estado atual da partida.
'''

import pygame as pg
import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8 #8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wP', 'wR', 'wQ', 'wN', 'wK', 'wB', 
              'bP', 'bR', 'bQ', 'bN', 'bK', 'bB']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color('white'))
    ms = ChessEngine.matchState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = [] 
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                sqSelected = (row, col)
            else:
                sqSelected = (row, col)
                playerClicks.append(sqSelected)
            if len(playerClicks) == 2:
                pass

        drawMatchState(screen, ms)
        clock.tick(MAX_FPS)
        pg.display.flip()

def drawMatchState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [pg.Color('white'), pg.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) %2 )]
            pg.draw.rect(screen, color, pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

main()
