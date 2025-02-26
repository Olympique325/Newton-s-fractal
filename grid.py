from newtons_method import newton
from complex import Complex
from values import f, fder, roots, WINDOW_HEIGHT, WINDOW_WIDTH

def create_grid(height:int, width:int,scale_x:float,scale_y:float) -> list:
    grid = []
    for line in range(height):
        new_line = []
        for column in range(width):
            scaled_x = ((column - width // 2) / width) * scale_x
            scaled_y = ((height // 2 - line) / height) * scale_y
            position = Complex(scaled_x, scaled_y)
            new_line.append(position)
        grid.append(new_line)
    return grid

def assign_root(grid:list) -> None:
    grid_size = WINDOW_HEIGHT * WINDOW_WIDTH
    counter = 0
    for line in grid:
        for column in range(len(line)):
            print(counter," / ",grid_size," (",round((counter/grid_size)*100,2),"%)",sep="")
            counter += 1
            position = line[column]
            root_approx = newton(position,f,fder)

            closest_root = roots[0]
            closest_distance = abs(root_approx - closest_root)
            for root in roots[1:]:
                distance = abs(root_approx - root)
                if distance < closest_distance:
                    closest_root = root
                    closest_distance = distance

            line[column] = roots.index(closest_root)