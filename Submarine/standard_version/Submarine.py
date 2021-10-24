class Submarine:
    def __init__(self, x = 0, y = 0, z = 0, direction = 0):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__direction = direction
        self.__cardinal = ('NORTH', 'EAST', 'SOUTH', 'WEST')
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
    
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        self.__z = z
    
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction):
        self.__direction = direction
    
    @property
    def cardinal(self):
        return self.__cardinal

# ==========================================================================
    def command(self, comm):
        for letter in comm:
            if(letter == 'L' or letter == 'R'):
                self.turn(letter)
            elif(letter == 'U' or letter == 'D'):
                self.sink(letter)
            elif(letter == 'M'):
                self.move()
        
        result = f'{self.x} {self.y} {self.z} {self.cardinal[self.direction]}'
        return result

    def turn(self, letter):
        if(letter == 'L'):
            if(self.direction == 0):
                self.direction = 3
            else:
                self.direction -= 1
        else:
            if(self.direction == 3):
                self.direction = 0
            else:
                self.direction += 1

    def sink(self, letter):
        if(letter == 'D'):
            self.z -= 1
        else:
            self.z += 1

    def move(self):
        if(self.direction == 0):
            self.y += 1
        elif(self.direction == 1):
            self.x += 1
        elif(self.direction == 2):
            self.y -= 1
        elif(self.direction == 3):
            self.x -= 1