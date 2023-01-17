import pygame
import numpy as np

COLOR_DIE = (255, 255, 215)
COLOR_ALIVE = (255, 255, 215)
COLOR_BG = (10, 10, 40)
COLOR_GRID = (30, 30, 60)

def B3S23(screen, cells, size):
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))
    
    for row, col in np.ndindex(cells.shape):
        num_alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        if cells[row, col] == 1 and num_alive < 2 or num_alive > 3:
            color = COLOR_DIE
        elif cells[row, col] == 1 and 2 <= num_alive <= 3:
            update_cells[row, col] = 1
            color = COLOR_ALIVE
        else:
            if  cells[row, col] == 0 and num_alive == 3:
                update_cells[row, col] = 1
                color = COLOR_ALIVE


        color = color if cells[row, col] == 1 else COLOR_BG
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return update_cells

def B36S23(screen, cells, size):
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))
    

    for row, col in np.ndindex(cells.shape):
        num_alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]

        if num_alive < 2 or num_alive > 3 and num_alive != 6:
            update_cells[row, col] = 0
            color = COLOR_DIE
        elif cells[row, col] == 1 and num_alive == 2 or num_alive == 3:
            update_cells[row, col] = 1
            color = COLOR_ALIVE
        else:
            if  cells[row, col] == 0 and num_alive == 3 or num_alive == 6:
                update_cells[row, col] = 1
                color = COLOR_ALIVE
            if  (num_alive == 2) or (cells[row, col] == 1 and num_alive == 6):
                update_cells[row, col] = 0
                color = COLOR_DIE


        color = color if cells[row, col] == 1 else COLOR_BG
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return update_cells


def glider(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0, 1, 0],
                        [0, 0, 1],
                        [1, 1, 1]]);
    pos = (8,8)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern

    return cells

def pulsar(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],     
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     
                         [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],     
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     
                         [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]]);
    pos = (8,8)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern

    return cells

def gosper(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pos = (15,20)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    
    return cells
def replicator(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    pattern = np.array([[0, 0, 1, 1, 1],
                        [0, 1, 0, 0, 1],
                        [1, 0, 0, 0, 1],
                        [1, 0, 0, 1, 0],
                        [1, 1, 1, 0, 0]]);         
    pos = (30,30)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    
    return cells


def bomber(dimx, dimy):
    cells = np.zeros((dimy, dimx))
    
    pattern = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 0, 0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0]]); 

    pos = (8,8)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    
    return cells 


def main(dimx, dimy, cellsize):
    
    print('/////Game of Life/////')
    regra = input('Digite a regra desejada. 1 - B3/S26  ou 2 - B36/S23: ')

    if(regra == 1):
        padraoRegra1 = input('Escolha o padrao. 1 - Glider, 2 - Pulsar ou 3 - Gosper: ')
        if(padraoRegra1 == 1):
            cells = glider(dimx, dimy)
            cells = B3S23(surface, cells, cellsize)
        elif(padraoRegra1 == 2):
            cells = pulsar(dimx, dimy)
            cells = B3S23(surface, cells, cellsize)
        else: 
            if padraoRegra1 == 3:
                cells = gosper(dimx, dimy)
                cells = B3S23(surface, cells, cellsize)

    #cells = glider(dimx, dimy)
    #cells = pulsar(dimx, dimy)
    #cells = gosper(dimx, dimy)  
    #cells = replicator(dimx, dimy)  
    #cells = bomber(dimx, dimy)  

 
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Renan and Pedro's Game of Life")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(COLOR_GRID)

        cells = B3S23(surface, cells, cellsize)
        #cells = B36S23(surface, cells, cellsize)
        pygame.display.update()


if __name__ == "__main__":
    main(90, 70, 10)