"""Creates and displays the fractal graphic"""
from PIL import Image, ImageDraw

from values import colours, WINDOW_WIDTH, WINDOW_HEIGHT

def draw_point(x,y,grid,draw):
    index = grid[y][x]
    draw.point((x,y),colours[index])

def create_graphic(grid):
    im = Image.new("RGB",(WINDOW_WIDTH,WINDOW_HEIGHT))
    draw = ImageDraw.Draw(im, "RGB")

    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            draw_point(x,y,grid,draw)

    im.show("Test")