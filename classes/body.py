import pygame
import numpy as np

# CONSTANTS

TIME_DELAY = 0.001


class Body:
    def __init__(self, position_array, mass, color, radius=5):
        self.in_contact = False
        self.velocity = np.array([[0, 0, 0]])
        self.force = np.array([[0, 0, 0]])
        self.mass = mass
        self.position = position_array
        self.radius = radius
        self.thickness = radius * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position[0][0], self.position[0][1]), self.radius, self.thickness)

    def add_velocity(self, velocity_array):
        self.velocity = self.velocity + velocity_array

    def add_force(self, force_array):
        self.force = self.force + force_array

    def move(self):
        if self.in_contact:
            self.velocity = self.velocity * 0.05
            self.color = (255, 0, 0)
        else:
            self.color = (255, 255, 255)

        self.velocity = self.velocity + (self.force / self.mass) * TIME_DELAY
        self.position = self.position + self.velocity * TIME_DELAY
