import numpy as np
import asteroids_params

class Mover:

    def __init__( self, X, V, A ):

        self.X = X
        self.V = V
        self.A = A

    def move( self ):

        self.V += self.A
        self.X += self.V

        #self.X = self.X % np.array( [asteroids_params.LENGTH, asteroids_params.WIDTH] )


