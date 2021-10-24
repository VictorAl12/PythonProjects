from Submarine import Submarine

# x validation
def x_input():
    while True:
        try:
            x = int(input('X = '))
        except:
            print('X value must be a number.')
            continue
        break
    return x

# y validation
def y_input():
    while True:
        try:
            y = int(input('Y = '))
        except:
            print('Y value must be a number.')
            continue
        break
    return y

# z validation
def z_input():
    while True:
        try:
            z = int(input('Z = '))
            assert z <= 0
        except:
            print('Z value must be a number and zero or less.')
            continue
        break
    return z

# direction validation
def direction_input():
    cardinal = ('NORTH', 'EAST', 'SOUTH', 'WEST')
    while True:
        try:
            direction = input('Direction = ').upper()
            assert direction == 'NORTH' or direction == 'EAST' or direction == 'SOUTH' or direction == 'WEST'
        except:
            print('Direction must be North, South, East, or West.')
            continue
        break
    direction = cardinal.index(direction)
    return direction

# command validation
def comm_input():
    while True:
        try:
            comm = input('Commands: ').upper()
            for letter in comm:
                assert letter =='U' or letter == 'D' or letter == 'L' or letter == 'R'  or letter == 'M'
        except:
            print('Command must contain valid orders.')
            continue
        break
    return comm

# =============================================================================

def main():
    # starting positions
    print('''\nInsert the submarine's starting X, Y and Z positions as well 
as the cardinal direction that its facing.\n
        [NOTE: Z = 0 represents the water's surface]\n\n''')

    while True:
        try:
            default = input('Use default values (X = 0, Y = 0, Z = 0, Direction = NORTH)? [Y/N]: ').upper()
            assert default == 'Y' or default == 'N'
        except:
            print('Please, insert a valid response.\n')
            continue
        break
    
    if(default == 'Y'):
        # instancing object
        sub = Submarine()
    else:
        x = x_input()
        y = y_input()
        z = z_input()
        direction = direction_input()

        # instancing object
        sub = Submarine(x, y, z, direction)

    # command
    print('''\nInsert the submarine's movement orders (e.g. "LMRDDMMUU") 
    U = Up\n    D = Down\n    L = turn Left\n    R = turn Right\n    M = Move''')
    comm = comm_input()
    new_positon = sub.command(comm)
    print(f'\n\nThe submarine is now on {new_positon}')


if __name__ == '__main__':
    main()