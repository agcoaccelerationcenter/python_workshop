import Mover
import numpy as np
import asteroids_params
import pygame

class Player( Mover.Mover ):

    COLOR = asteroids_params.WHITE
    HEIGHT = 20
    ANGLE = 30
    BASE = np.arctan( np.radians(ANGLE) ) * HEIGHT
    CENTER_TO_TIP = HEIGHT / (2 *np.cos(np.radians(ANGLE/2))**2 )
    BASE_COORDS = np.array([
        [CENTER_TO_TIP, 0],
        [CENTER_TO_TIP - HEIGHT, BASE/2],
        [CENTER_TO_TIP - HEIGHT, -BASE/2]
        ])
    ROTATE_MAG = 3.5
    BOOST_MAG = .15

    def __init__( self, X=np.array( [asteroids_params.LENGTH/2, asteroids_params.WIDTH/2] ),
                        V=np.array( [0.0, 0.0] ),
                        A=np.array( [0.0, 0.0] ),
                        heading = 0
                ):

        super().__init__( X, V, A )
        self.heading = heading

    def rotate( self, dir ):

        """Change the heading of player"""

        self.heading += np.radians( dir*self.ROTATE_MAG )

    def boost( self ):

        """Add velocity in the direction of heading"""

        self.V += np.array( [ self.BOOST_MAG*np.cos(self.heading), self.BOOST_MAG*np.sin(self.heading) ] )

    def draw( self, screen ):
        
        """Draw the shooter"""

        rot_matrix = np.array( [ [np.cos(self.heading),-np.sin(self.heading)],[np.sin(self.heading),np.cos(self.heading)] ] )
        rotated_coords = np.matmul( rot_matrix, self.BASE_COORDS.T ).T
        translated_coords =  rotated_coords + self.X
        pygame.draw.polygon(screen, self.COLOR, translated_coords)