import classes

# Gets a valid map size
def size_input() :
    while True:
        size = input("What is the size of the 2d square maze? ")
        if size.isdigit() and int(size) > 0:
            return int(size)
        print("Invalid size, try again.")

# Gets the valid layout of the map
def layout_input(maze_size) :
    print("Give a line at a time, with each block as the character that needs to be used as the texture.\nFor example, ! would print a wall block of exclamation marks.")
    maze = []
    for i in range(maze_size) :
        while True:
            line = input("Line " + str(i + 1) + ": ")
            if len(line) == maze_size :
                break
            print("Given line is not the correct length.")
        maze.append(line)
    return maze

# Gets coordinates that the camera is in and the orientation
def location_input(size) :
    print("Location is seen from the top left, so the top left is (0,0) and the bottom right is (n,n).")
    while True:
        x_coordinate = input("What is the X-coordinate? ")
        if x_coordinate.isdigit() and -1 < int(x_coordinate) < size :
            break
        print("Invalid X-coordinate. Try again.")

    while True:
        y_coordinate = input("What is the Y-coordinate? ")
        if y_coordinate.isdigit() and -1 < int(y_coordinate) < size :
            break
        print("Invalid Y-coordinate. Try again.")

    facings = ["N", "E", "S", "W"]
    while True:
        orientation = input("What way is the camera facing?(N/E/S/W) ").upper()
        for i in range(4) :
            if orientation == facings[i] :
                return classes.CameraLocation(int(x_coordinate), int(y_coordinate), i)
        print("Invalid orientation. Try again.")