import pygame
import sys



BLANCO=(255,255,255)
ROJO=(255,0,0)
NEGRO=(0,0,0)
AMARILLO=(255,219,0)

ANCHO=800
ALTO=600


def get_line(start, end):


    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end


    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


pygame.init()
pantalla=pygame.display.set_mode([ANCHO,ALTO])



reloj=pygame.time.Clock()


fin = False
while not fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
            pygame.quit()
            sys.exit()

    pantalla.fill(BLANCO)
    mouse= pygame.mouse.get_pos()
    linea=get_line((ANCHO/2-100,ALTO/2),(mouse))
    pygame.draw.circle(pantalla,NEGRO,(ANCHO/2-100,ALTO/2),50,5)
    pygame.draw.circle(pantalla,NEGRO,(linea[20]),20)

    linea2=get_line((ANCHO/2,ALTO/2),(mouse))
    pygame.draw.circle(pantalla,NEGRO,(ANCHO/2,ALTO/2),50,5)
    pygame.draw.circle(pantalla,NEGRO,(linea2[20]),20)

    pygame.display.flip()


reloj.tick(60)
