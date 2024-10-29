import sys
import pygame
from constants import *
#from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group,drawable_group)

    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group,updatable_group,drawable_group)
    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()

    shot_group = pygame.sprite.Group()
    Shot.containers = (shot_group,updatable_group,drawable_group)
    
    fps_clock = pygame.time.Clock()
    dt = 0

    player_object = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen,(0,0,0))
        for group_object in updatable_group:
            group_object.update(dt)

        for group_object in asteroid_group:
            if player_object.check_collision(group_object):
                print("Game over!")
                sys.exit()
        for shot_object in shot_group:
            for asteroid_object in asteroid_group:
                if shot_object.check_collision(asteroid_object):
                    shot_object.kill()
                    asteroid_object.split()

        for group_object in drawable_group:
            group_object.draw(screen)
        
        pygame.display.flip()
        dt = fps_clock.tick(59) /1000
        #print(player_object.position)
if __name__ == "__main__":
    main()
