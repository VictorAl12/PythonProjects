class Submarino:
    def __init__(self, x = 0, y = 0, z = 0, direcao = 0):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__direcao = direcao
        self.__cardinal = ('NORTE', 'LESTE', 'SUL', 'OESTE')
    
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
    def direcao(self):
        return self.__direcao
    @direcao.setter
    def direcao(self, direcao):
        self.__direcao = direcao
    
    @property
    def cardinal(self):
        return self.__cardinal

# ==========================================================================
    def comandar(self, comm):
        for letra in comm:
            if(letra == 'L' or letra == 'R'):
                self.girar(letra)
            elif(letra == 'U' or letra == 'D'):
                self.aprofundar(letra)
            elif(letra == 'M'):
                self.mover()
        
        result = f'{self.x} {self.y} {self.z} {self.cardinal[self.direcao]}'
        return result

    def girar(self, letra):
        if(letra == 'L'):
            if(self.direcao == 0):
                self.direcao = 3
            else:
                self.direcao -= 1
        else:
            if(self.direcao == 3):
                self.direcao = 0
            else:
                self.direcao += 1

    def aprofundar(self, letra):
        if(letra == 'D'):
            self.z -= 1
        else:
            self.z += 1

    def mover(self):
        if(self.direcao == 0):
            self.y += 1
        elif(self.direcao == 1):
            self.x += 1
        elif(self.direcao == 2):
            self.y -= 1
        elif(self.direcao == 3):
            self.x -= 1