from grid import create_grid, assign_root
from display import create_graphic
from values import WINDOW_HEIGHT, WINDOW_WIDTH, SCALE_X, SCALE_Y
from time import sleep,time

def main() -> None:
    start_time = time()
    print("Creating grid...")
    grid = create_grid(WINDOW_HEIGHT,WINDOW_WIDTH,SCALE_X,SCALE_Y)
    print("Running calculations...")
    sleep(3)
    assign_root(grid)
    print("Done!")
    total_seconds = time() - start_time
    print("Fractal generated in:",total_seconds//60,"minutes",round(total_seconds % 60),"seconds")
    sleep(3)
    create_graphic(grid)


__version__ = "1.0"

if __name__ == '__main__':
    main()