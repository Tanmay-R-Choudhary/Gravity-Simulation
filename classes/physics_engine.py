import numpy as np


def _magnitude(arr):
    return np.sqrt(pow(arr[0], 2) + pow(arr[1], 2) + pow(arr[2], 2))


def _unit_vector(arr):
    mag = _magnitude(arr)
    return np.array([
        [
            arr[0] / mag,
            arr[1] / mag,
            arr[2] / mag,
        ]
    ])


class PhysicsEngine:
    def __init__(self):
        self.body_pos_array = np.array([]).reshape((0, 3))
        self.body_list = None

    def define_bodies(self, *args):
        self.body_list = [np.array([i, body]) for i, body in enumerate(args[0])]

    def compute_force_vectors(self):
        distance_list = []
        force_list = []
        net_force = []

        for primary_body in self.body_list:
            temp = np.array([]).reshape((0, 3))
            for secondary_body in self.body_list:
                temp = np.append(
                    temp,
                    (primary_body[1].position - secondary_body[1].position) * np.array([[-1, -1, 1]]),
                    axis=0
                )
            distance_list.append(temp)
            temp = np.array([]).reshape((0, 3))

        for primary_body in self.body_list:
            temp = np.array([]).reshape((0, 3))
            for secondary_body in self.body_list:
                if _magnitude(distance_list[primary_body[0]][secondary_body[0]]) != 0:
                    force = 6.67 * pow(10, -11) * primary_body[1].mass * secondary_body[1].mass * (
                            1 / pow(_magnitude(distance_list[primary_body[0]][secondary_body[0]]) * 0.25, 2))
                    force = force * _unit_vector(distance_list[primary_body[0]][secondary_body[0]])
                    temp = np.append(
                        temp,
                        force * np.array([[1, 1, 1]]),
                        axis=0
                    )
                else:
                    temp = np.append(
                        temp,
                        np.array([[0.0, 0.0, 0.0]]),
                        axis=0
                    )
            force_list.append(temp)
            temp = np.array([]).reshape((0, 3))

        # print(force_list)
        for obj in force_list:
            net_force.append(obj.sum(axis=0))

        # print(net_force)
        return net_force
