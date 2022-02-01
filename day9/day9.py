import functools
def main(data):
    dimRow = len(data)
    dimCol = len(data[0])

    risk_sum = 0
    visited = set()
    basins = []
    for i in range(dimRow):
        for j in range(dimCol):
            # Part 1 
            # if checkNeighbours(i, j, dimRow, dimCol, data):
            #     risk_sum += int(data[i][j]) + 1
            # Part 2
            if (i,j) not in visited and int(data[i][j]) != 9:
                basins.append(expandBasin(i, j, dimRow, dimCol, data, visited))
    top_3 = sorted(basins)[-3:]
    print(functools.reduce(lambda x, y: x*y,top_3))
def checkNeighbours(row, col, dimRow, dimCol, arr):
    # if row < 0 or col < 0 or row >= dimRow or col >= dimCol:
    #     return True
    val = int(arr[row][col])
    if row-1 >= 0:
        if int(arr[row-1][col]) <= val:
            return False
    if row+1 < dimRow:
        if int(arr[row+1][col]) <= val:
            return False
    if col-1 >= 0:
        if int(arr[row][col-1]) <= val:
            return False
    if col+1 < dimCol:
        if int(arr[row][col+1]) <= val:
            return False
    return True

def expandBasin(row,col,dimRow,dimCol,arr,visited):
    if row < 0 or col < 0 or row >= dimRow or col >= dimCol or (row,col) in visited or int(arr[row][col]) == 9:
        return 0
    else:
        visited.add((row,col))
        return 1 + expandBasin(row-1,col,dimRow,dimCol,arr,visited) + expandBasin(row+1,col,dimRow,dimCol,arr,visited) + expandBasin(row,col-1,dimRow,dimCol,arr,visited) + expandBasin(row,col+1,dimRow,dimCol,arr,visited)
    

if __name__ == "__main__":
    with open("day9_input.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
