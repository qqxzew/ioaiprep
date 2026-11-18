import numpy as np
import time 


grid = np.zeros((5, 5), dtype=int)

grid[[2, 2, 2], [1, 2, 3]] = 1
y, x = 2, 5
def neighbor(grid , y: int, x: int) -> int:
    rows, cols = grid.shape
    neighbor_count = 0      
    for dy in range(y-1, y+2):
        for dx in range(x-1, x+2):
            if dx == x and dy == y:
                continue
            else:
                if dx < 0 or dy < 0:
                    continue 
                if dy >= rows or dx >= cols:
                    continue
                neighbor_count += grid[dy, dx]
    return neighbor_count
print(neighbor(grid, y, x))
