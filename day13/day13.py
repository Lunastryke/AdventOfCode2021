def main(data):
    sep = data.index('')
    coords = data[0:sep]
    instructions = data[sep+1::]
    grid = set()
    for ele in coords:
        x, y = ele.split(',')
        grid.add((int(x),int(y)))
    x_len = 0
    y_len = 0
    for instr in instructions:
        axis, val = instr[11::].strip().split("=")
        val =  int(val)
        to_remove = set()
        to_add = set()
        if axis == 'x':
            x_len = val
            for coord in grid:
                x,y = coord
                if x >= val:
                    to_remove.add((x,y))
                    to_add.add((val-(x-val),y))
        else:
            y_len = val
            for coord in grid:
                x,y = coord
                if y >= val:
                    to_remove.add((x,y))
                    to_add.add((x,val-(y-val)))
        for i in to_remove:
            grid.remove(i)
        for i in to_add:
            grid.add(i)
    print(len(grid))
    for i in range(y_len):
        to_print = ''
        for j in range(x_len):
            if (j,i) in grid:
                to_print += '#'
            else:
                to_print += '.'
        print(to_print)

if __name__ == "__main__":
    with open("day13_input.txt", 'r') as file:
        data = file.read().splitlines()
    main(data)
