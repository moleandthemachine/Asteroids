import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0,0)

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        a_vel1 = self.velocity.rotate(random_angle)
        a_vel2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,new_radius)
        a1.velocity = 1.2*a_vel1
        a2 = Asteroid(self.position.x,self.position.y,new_radius)
        a2.velocity = 1.2*a_vel2

