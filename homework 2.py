import numpy as np

def new_state(array):
    array_padded = np.pad(array, 1)
    updated_array=array.copy()
    
    for x in range(1, array.shape[0]+1):
        for y in range(1, array.shape[1]+1):
            cell = array[x-1][y-1]
            neighbours = (array_padded[x-1][y-1], array_padded[x][y-1],
                          array_padded[x+1][y-1], array_padded[x+1][y],
                          array_padded[x+1][y+1], array_padded[x][y+1],
                          array_padded[x-1][y+1], array_padded[x-1][y])
            neighbours_count = sum(neighbours)
            
            if cell == 1 and (neighbours_count < 2 or neighbours_count > 3):
                updated_array[x-1, y-1] = 0
            elif cell == 0 and neighbours_count == 3:
                updated_array[x-1, y-1] = 1
                
    return updated_array

arrayNew = np.random.randint(2, size=(7,7))

new_state(arrayNew)
