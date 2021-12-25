import pygame
import time
from src.classes.physics_engine import PhysicsEngine


class Simulation:
    physics_engine = PhysicsEngine()

    def __init__(self):
        self.run, self.space, self.bodies = None, None, None

    def initialise_environment(self, body_list):
        self.bodies = body_list
        space_plane_size = (1000, 800)  # width, height of canvas
        self.run = True

        # setting up pygame
        pygame.init()
        pygame.display.set_caption("Orbit simulator")
        self.space = pygame.display.set_mode(space_plane_size)

        # setting up physics engine
        self.physics_engine.define_bodies(body_list)

    def show_environment(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.space.fill((0, 0, 0))

            net_force = self.physics_engine.compute_force_vectors()
            for i, body in enumerate(self.bodies):
                body.force = net_force[i]

            for body in self.bodies:
                body.draw(self.space)

            for body in self.bodies:
                body.move()
                # print(body.velocity)
                # print(body.position)
            time.sleep(0.0005)
            pygame.display.update()
            # self.run = False
