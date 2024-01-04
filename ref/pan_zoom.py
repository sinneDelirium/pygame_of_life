# Source: https://stackoverflow.com/questions/17680285/pygame-viewport-click-drag

import pygame, sys, math
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
GRIDSIZE = 256
TILESIZE = 40
BGCOLOR = (128, 128, 128)
FGCOLOR = (64, 64, 64)

GRID = []

FPSCLOCK = pygame.time.Clock()

indexX = None
indexY = None

minVPcoordX = 0
minVPcoordY = 0
maxVPcoordX = (TILESIZE*GRIDSIZE)-WINDOWWIDTH
maxVPcoordY = (TILESIZE*GRIDSIZE)-WINDOWHEIGHT
viewportOffset = (0, 0)
vpStartXTile = 0
vpStartYTile = 0
viewportCoord = (0, 0)

coordX = 0
coordY = 0

def main():
    global FPSCLOCK, DISPLAYSURF
    global coordX, coordY
    global offsetX, offsetY, negativeOffsetX, negativeOffsetY
    global movedDistanceX, movedDistanceY
    global isDragging

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mouseX = 0
    mouseY = 0

    generateGrid(GRIDSIZE, GRIDSIZE)

    isDragging = False
    mousePos = (0, 0)
    dragStart = (0,0)
    dragEnd = (0,0)

    pygame.font.init()
    arialFnt = pygame.font.SysFont('Arial', 16)
    while True:
        DISPLAYSURF.fill(BGCOLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 2:
                    isDragging = True
                elif event.button == 4:
                    zoomIn()
                elif event.button == 5:
                    zoomOut()
            elif event.type == MOUSEMOTION:
                mouseRel = pygame.mouse.get_rel()
                moveGrid(mouseRel)
            elif event.type == MOUSEBUTTONUP:
                isDragging = False

        viewportCoord = (coordX, coordY)

        vpStartXTile = math.floor(float(viewportCoord[0]/TILESIZE))
        vpStartYTile = math.floor(float(viewportCoord[1]/TILESIZE))
        GRIDstartTile = GRID[vpStartXTile][vpStartYTile]

        negativeOffsetX = viewportCoord[0] - GRID[vpStartXTile][vpStartYTile][0]
        negativeOffsetY = viewportCoord[1] - GRID[vpStartXTile][vpStartYTile][1]

        offsetX = TILESIZE - negativeOffsetX
        offsetY = TILESIZE - negativeOffsetY

        repeatX = math.floor(WINDOWWIDTH/TILESIZE)
        repeatY = math.floor(WINDOWHEIGHT/TILESIZE)

        drawGrid(repeatX, repeatY)

        outputLabel = arialFnt.render('(Top-Left)Coordinates: x%s - y%s' % (coordX, coordY), 1, (255,255,255))
        DISPLAYSURF.blit(outputLabel, (10, 10))

        # frame draw
        pygame.display.set_caption("Memory Game - FPS: %.0f" % FPSCLOCK.get_fps())
        pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def generateGrid(xTiles=None, yTiles=None):
    global GRID

    GRID = []

    for i in range(xTiles):
        GRID.append([None] * yTiles)

    ix = 0
    iy = 0

    posX = -40

    for x in range(len(GRID[ix])):
        posX += TILESIZE
        posY = -40
        iy = 0
        for y in range(xTiles):
            posY += TILESIZE
            position = (posX, posY)
            GRID[ix][iy] = position
            iy += 1
        if ix < xTiles:
            ix += 1
        else:
            return

def drawGrid(x=None, y=None):
    lineWidth = 1

    xPos = 0
    yPos = 0

    for i in range(x):
        xStart = (xPos + offsetX, 0)
        xEnd = (xPos + offsetX, WINDOWHEIGHT + negativeOffsetY)
        pygame.draw.line(DISPLAYSURF, FGCOLOR, xStart, xEnd, lineWidth)
        xPos += TILESIZE

    for i in range(y):
        yStart = (0, yPos + offsetY)
        yEnd = (WINDOWWIDTH + negativeOffsetX, yPos + offsetY)
        pygame.draw.line(DISPLAYSURF, FGCOLOR, yStart, yEnd, lineWidth)
        yPos += TILESIZE

def moveGrid(rel):
    global coordX, coordY, isDragging


    if isDragging == True:
        #X
        if coordX <= maxVPcoordX and coordX >= minVPcoordX:
            coordX = coordX - rel[0]
            if coordX > maxVPcoordX:
                coordX = maxVPcoordX
            if coordX < minVPcoordX:
                coordX = 0
        #Y   
        if coordY <= maxVPcoordY and coordY >= minVPcoordY:
            coordY = coordY - rel[1]
            if coordY > maxVPcoordY:
                coordY = maxVPcoordY
            elif coordY < minVPcoordY:
                coordY = 0
    #-------------



def zoomIn():
    global TILESIZE, maxVPcoordX, maxVPcoordY

    TILESIZE += 4

    print("Tile size: ", TILESIZE)

    generateGrid(GRIDSIZE, GRIDSIZE)

    maxVPcoordX = (TILESIZE*GRIDSIZE)-WINDOWWIDTH
    maxVPcoordY = (TILESIZE*GRIDSIZE)-WINDOWHEIGHT


def zoomOut():
    global TILESIZE, maxVPcoordX, maxVPcoordY

    TILESIZE -= 4
    if TILESIZE <= 0:
        TILESIZE = 4

    print("Tile size: ", TILESIZE)

    generateGrid(GRIDSIZE, GRIDSIZE)

    maxVPcoordX = (TILESIZE*GRIDSIZE)-WINDOWWIDTH
    maxVPcoordY = (TILESIZE*GRIDSIZE)-WINDOWHEIGHT


main()
