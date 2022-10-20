import Mover
import numpy as np
import asteroids_params
import pygame

class Asteroid( Mover.Mover ):

    MAX_SPEED = 0.6
    
    def __init__( self, radius = 10 ):

        X = np.array( [np.random.random()*asteroids_params.LENGTH, np.random.random()*asteroids_params.WIDTH] )
        V = np.array( [ (-0.5+np.random.random())*self.MAX_SPEED, (-0.5+np.random.random())*self.MAX_SPEED] )
        A = np.array( [0.0, 0.0] )

        super().__init__( X, V, A )
        self.radius = 10
        self.color = asteroids_params.WHITE

    def draw( self, screen ):

        pygame.draw.circle(screen, self.color, [int(self.X[0]), int(self.X[1])], self.radius)