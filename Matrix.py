from Vector import Vector

class Matrix:
    matrix = []
    nxn = 3
    
    def __init__(self, _n):
        self.nxn = _n
        for i in range(self.nxn):
            arr = []
            for j in range(self.nxn):
                arr.append(2.0)
            self.matrix.append(arr)
    
    def __add__(self, m):
        aux = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(self.nxn):
            for j in range(self.nxn):
                aux[i][j] += self.matrix[i][j] + m.matrix[i][j]
        return aux
    
    def __mul__(self, m): #Matriz por matriz *
        aux = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(self.nxn):
            for j in range(self.nxn):
                for k in range(self.nxn):
                    aux[i][j] += self.matrix[i][k] * m.matrix[k][j]
        return aux
    
    def __xor__(self, vec): #Matriz por vector ^ (Alt+94)
        mat = [[0], [0], [0]]
        mat[0][0] = vec.x
        mat[1][0] = vec.y
        mat[2][0] = vec.z
        sum = 0
        aux = [[0], [0], [0]]
        
        for i in range(self.nxn):
            for j in range(self.nxn):
                for k in range(self.nxn):
                    sum += self.matrix[i][k] * mat[k][0]
                aux[i][0] = sum
                sum = 0
        return aux
        
    def __pow__(self, num): #Matriz por escalar (%)
        aux = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
        for i in range(self.nxn):
            for j in range(self.nxn):
                aux[i][j] = self.matrix[i][j] * num 
        return aux
        
    def __str__(self): #Imprimir una matriz
        output = ""
        for i in range(self.nxn):
            for j in range(self.nxn):
                output += "["+ str(self.matrix[i][j]) +"]"
            output += "\n"
        return output
    
    def Identity(self):
        for i in range(self.nxn):
            for j in range(self.nxn):
                if(i == j):
                    self.matrix[i][j] = 1
        return self.matrix











              