def main(data, num_rounds):
    rowDim = len(data)
    colDim = len(data[0])
    total = rowDim * colDim
    # Enter code here
    def propogateFlash(row,col):
        if row < 0 or col < 0 or row >= rowDim or col >= colDim or (row,col) in flashed:
            return 0
        data[row][col] += 1
        if data[row][col] > 9:
            flashed.add((row,col))
            return 1 + propogateFlash(row-1,col) + propogateFlash(row-1, col-1) + propogateFlash(row-1, col+1) + propogateFlash(row+1, col) + propogateFlash(row+1, col-1) + propogateFlash(row+1, col+1) + propogateFlash(row, col-1) + propogateFlash(row, col + 1) 
        return 0

    flashes = 0
    # Part 1
    # for x in range(num_rounds):
    rounds = 0
    while True:
        flashed = set()
        curr_flashes = 0
        for row in range(rowDim):
            for col in range(colDim):
                curr_flashes += propogateFlash(row,col)
        for coord in flashed:
            row_coord, col_coord = coord
            data[row_coord][col_coord] = 0
        rounds += 1
        if curr_flashes == total:
            print(rounds)
            return
        flashes += curr_flashes


    print("Flashes: ", flashes)

if __name__ == "__main__":
    with open("day11_input.txt", 'r') as file:
        data = file.read().splitlines()
    processed_data = [[int(i) for i in row] for row in data]
    num_rounds = int(input("Enter number of rounds to run for: "))
    main(processed_data, num_rounds)
