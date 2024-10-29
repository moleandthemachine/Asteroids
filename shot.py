import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,velocity):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius)

    def update(self, dt):
        self.position += self.velocity*dt*PLAYER_SHOOT_SPEED
       
