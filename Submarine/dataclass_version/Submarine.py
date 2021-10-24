from dataclasses import dataclass

cardinal = ('NORTH', 'EAST', 'SOUTH', 'WEST')

# NOTE: in this version all attributes had to be mutable and unprotected
@dataclass(frozen=False)
class Submarine:
    x: int = 0
    y: int = 0
    z: int = 0
    direction: int = 0

# ==========================================================================
    def command(self, comm):
        for letter in comm:
            if(letter == 'L' or letter == 'R'):
                self.turn(letter)
            elif(letter == 'U' or letter == 'D'):
                self.sink(letter)
            elif(letter == 'M'):
                self.move()
        
        result = f'{self.x} {self.y} {self.z} {cardinal[self.direction]}'
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