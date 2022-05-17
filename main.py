import numpy as np
from src.classes.body import Body
from src.classes.simulation import Simulation


# erratic orbits that result in one body off-screen and two bodies in stable binary system that also moves off screen
body1 = Body(np.array([[500, 300, 0]]), 6 * pow(10, 15), (255, 255, 255))
body1.add_velocity(np.array([[40, 0, 0]]))

body2 = Body(np.array([[600, 200, 0]]), 6 * pow(10, 15), (0, 0, 255))
body2.add_velocity(np.array([[-40, 0, 0]]))

body3 = Body(np.array([[300, 500, 0]]), 6 * pow(10, 15), (0, 255, 0))
body3.add_velocity(np.array([[50, 0, 0]]))

sim = Simulation()
sim.initialise_environment([body1, body2, body3])
sim.show_environment()

# ------------------------------------#

# stable circular orbit
# body1 = Body(np.array([[500, 400, 0]]), 6 * pow(10, 15), (255, 255, 255))
#
# body2 = Body(np.array([[500, 600, 0]]), 6 * pow(10, 9), (0, 0, 255))
# body2.add_velocity(np.array([[200, 0, 0]]))
#
# sim = Simulation()
# sim.initialise_environment([body1, body2])
# sim.show_environment()

# ------------------------------------#

# stable elliptical orbit
# body1 = Body(np.array([[500, 400, 0]]), 6 * pow(10, 15), (255, 255, 255))
#
# body2 = Body(np.array([[500, 500, 0]]), 6 * pow(10, 9), (0, 0, 255))
# body2.add_velocity(np.array([[200, 0, 0]]))
#
# sim = Simulation()
# sim.initialise_environment([body1, body2])
# sim.show_environment()

# ------------------------------------#

# stable binary star system
# MASS = 6 * pow(10, 15)
# SPEED = 200
#
# body1 = Body(np.array([[500, 350, 0]]), MASS, (255, 255, 255))
# body1.add_velocity(np.array([[-1 * SPEED, 0, 0]]))
#
# body2 = Body(np.array([[500, 450, 0]]), MASS, (0, 0, 255))
# body2.add_velocity(np.array([[SPEED, 0, 0]]))
#
# sim = Simulation()
# sim.initialise_environment([body1, body2])
# sim.show_environment()

# ------------------------------------#

# I don't know if this exists. Looks good though!
# body1 = Body(np.array([[500, 300, 0]]), 6 * pow(10, 15), (255, 255, 255))
# body1.add_velocity(np.array([[-100, 0, 0]]))
#
# body2 = Body(np.array([[400, 400, 0]]), 6 * pow(10, 15), (0, 0, 255))
# body2.add_velocity(np.array([[0, 100, 0]]))
#
# body3 = Body(np.array([[500, 500, 0]]), 6 * pow(10, 15), (0, 255, 0))
# body3.add_velocity(np.array([[100, 0, 0]]))
#
# body4 = Body(np.array([[600, 400, 0]]), 6 * pow(10, 15), (255, 0, 0))
# body4.add_velocity(np.array([[0, -100, 0]]))
#
# sim = Simulation()
# sim.initialise_environment([body1, body2, body3, body4])
# sim.show_environment()