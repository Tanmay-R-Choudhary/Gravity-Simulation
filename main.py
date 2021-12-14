import numpy as np
from src.classes.body import Body
from src.classes.simulation import Simulation


body1 = Body(np.array([[500, 300, 0]]), 6 * pow(10, 15), (255, 255, 255))
body1.add_velocity(np.array([[40, 0, 0]]))

body2 = Body(np.array([[600, 200, 0]]), 6 * pow(10, 15), (0, 255, 0))
body2.add_velocity(np.array([[-40, 0, 0]]))

body3 = Body(np.array([[300, 500, 0]]), 6 * pow(10, 15), (255, 0, 0))
body3.add_velocity(np.array([[50, 0, 0]]))

sim = Simulation()
sim.initialise_environment(body1, body2, body3)
sim.show_environment()
