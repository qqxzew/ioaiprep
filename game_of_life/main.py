import os

import numpy as np
import time

grid = np.zeros((17, 17), dtype=int)


pulsar_q = [
    (2, 4), (2, 5), (2, 6),
    (4, 2), (5, 2), (6, 2),
    (4, 7), (5, 7), (6, 7),
    (7, 4), (7, 5), (7, 6)
]

for y, x in pulsar_q:
    grid[y, x] = 1
    grid[y, 16 - x] = 1
    grid[16 - y, x] = 1
    grid[16 - y, 16 - x] = 1


def neighbor(grid: np.ndarray , y: int, x: int) -> int:
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
def step(grid: np.ndarray) -> np.ndarray:
    new_grid = grid.copy()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            n_count = neighbor(grid, y, x)
            if grid[y][x] == 1:
                if n_count < 2 or n_count > 3:
                    new_grid[y][x] = 0
            else:
                if n_count == 3:
                    new_grid[y][x] = 1
    return new_grid 
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  
    for row in grid:
        print("".join("⬛" if cell else "⬜" for cell in row))
    grid = step(grid)
    time.sleep(0.5)
