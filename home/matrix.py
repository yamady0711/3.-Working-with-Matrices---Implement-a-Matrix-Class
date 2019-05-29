import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1: # for 1x1 matrix
            return self.g[0][0]
        elif self.h == 2: # for 2x2 matrix, simple calculation "ad - bc"
            return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]

    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        value = 0
        for i in range(self.h):
            value += self.g[i][i]  # sum of diagonal entries
        return value
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        det = self.determinant()
        if self.h == 1: #f or  1x1 case
            return Matrix([[1/det]])
        elif self.h == 2: # for 2x2 case
            return Matrix([[self.g[1][1]/det, -self.g[0][1]/det],[-self.g[1][0]/det, self.g[0][0]/det]])
           

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for i in range(self.w): # height of transpose = width of original
            newrow = []
            for j in range(self.h): # width of transpose = height of original
                newrow.append(self.g[j][i])  # transpose_i,j = original_j,i 
            matrix_transpose.append(newrow)
        return Matrix(matrix_transpose)
    

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        addition = []
        for i in range(self.h):
            newrow = []
            for j in range(self.w):
                newrow.append(self.g[i][j] + other.g[i][j])
            addition.append(newrow)
        return Matrix(addition)    
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        nega = []
        for i in range(self.h):
            newrow = []
            for j in range(self.w):
                newrow.append(-1. * self.g[i][j])
            nega.append(newrow)
        return Matrix(nega)    

    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be substituted if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        other_minus = -other  # utilize "-" operator
        return self + other_minus  # utilize "+" oeprator

    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #        
        other_transpose = other.T()  # utilize transpose function
        
        product = []
        for i in range(self.h):
            newrow = []
            for j in range(other_transpose.h):
                value = 0
                for k in range(self.w): # for-loop instead of calling "dot product function"
                    value += self.g[i][k] * other_transpose.g[j][k]
                newrow.append(value)
            product.append(newrow)
        return Matrix(product)        

        
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            product = []
            for i in range(self.h):
                newrow = []
                for j in range(self.w):
                    newrow.append(self.g[i][j]*other)
                product.append(newrow)
            return Matrix(product)
            
            
            
            
            