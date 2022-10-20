import pygame
import asteroids_params 
import time

import Player
import Asteroid

###### Setup
screen = pygame.display.set_mode( ( asteroids_params.LENGTH, asteroids_params.WIDTH ) )
clock = pygame.time.Clock()

###### Colors

###### MAIN LOOP
running = True

player_inst = Player.Player()
asteroids = []
last_created_asteroid = time.time()
last_deleted_asteroid = time.time()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill( asteroids_params.BLACK )


    if pygame.key.get_focused():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            running = False
        if keys[pygame.K_UP]:
            player_inst.boost()
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_LEFT]:
            player_inst.rotate( -1 )
        if keys[pygame.K_RIGHT]:
            player_inst.rotate( 1 )
        if keys[pygame.K_SPACE]:
            pass
        if keys[pygame.K_a]:
            # Add new asteroid
            if time.time() - last_created_asteroid > .25:
                asteroids.append( Asteroid.Asteroid() )            
                last_created_asteroid = time.time()
        if keys[pygame.K_s]:
            pass
        if keys[pygame.K_d]:
            # Delete an asteroid
            if len(asteroids) > 0:
                if time.time() - last_deleted_asteroid > .25:
                    del asteroids[-1]
                    last_deleted_asteroid = time.time()
    
    ### Move
    player_inst.move()
    for asteroid in asteroids:
        asteroid.move()

    ### Draw
    player_inst.draw( screen )
    for asteroid in asteroids:
        asteroid.draw( screen )

    ###

    pygame.display.flip()
    clock.tick( asteroids_params.FPS )