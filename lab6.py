import numpy as np

from lab5 import Lab5Renderer


def translate(dx, dy, dz):
    return np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])


def rotate_y(theta):
    rad = np.radians(theta)
    return np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])

def rotate_z(theta):
    rad = np.radians(theta)
    return np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def model_transform(dx, dy, dz, theta_y, theta_z=0):
    return np.matmul(np.matmul(translate(dx, dy, dz), rotate_y(theta_y)), rotate_z(theta_z))


class Lab6Renderer(Lab5Renderer):
    title = "Lab 6: Hierarchical Transformations"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.posz = -20
        self.carx = 0
        self.tirez = 0

    def poll_keys(self):
        super().poll_keys()
        if self.key_pressed[self.keys.H]:  # Return home
            self.posz = -20
            self.carx = 0
            self.tirez = 0

    def render_scene(self, delta_time):
        car_matrix = model_transform(self.carx, -4, 0, 0)
        tire1 = np.matmul(car_matrix, model_transform(-2, 0, 1.5, 0, self.tirez))
        tire2 = np.matmul(car_matrix, model_transform(2, 0, 1.5, 0, self.tirez))
        tire3 = np.matmul(car_matrix, model_transform(-2, 0, -1.5, 0, self.tirez))
        tire4 = np.matmul(car_matrix, model_transform(2, 0, -1.5, 0, self.tirez))

        self.car.render(car_matrix.T, color=np.array([0, 0, 255]))
        self.tire.render(tire1.T, color=np.array([0, 255, 0]))
        self.tire.render(tire2.T, color=np.array([0, 255, 0]))
        self.tire.render(tire3.T, color=np.array([0, 255, 0]))
        self.tire.render(tire4.T, color=np.array([0, 255, 0]))

        # Back row
        self.house.render(model_transform(-15, 0, -15, 90).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(-15, 0, 0, 90).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(-15, 0, 15, 90).T, color=np.array([255, 0, 0]))

        # First row
        self.house.render(model_transform(0, 0, 15, 180).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(0, 0, -15, 0).T, color=np.array([255, 0, 0]))

        # Second row
        self.house.render(model_transform(15, 0, 15, 180).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(15, 0, -15, 0).T, color=np.array([255, 0, 0]))

        # Third row
        self.house.render(model_transform(30, 0, 15, 180).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(30, 0, -15, 0).T, color=np.array([255, 0, 0]))

        # Fourth row
        self.house.render(model_transform(45, 0, 15, 180).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(45, 0, -15, 0).T, color=np.array([255, 0, 0]))

        # Fifth row
        self.house.render(model_transform(60, 0, 15, 180).T, color=np.array([255, 0, 0]))
        self.house.render(model_transform(60, 0, -15, 0).T, color=np.array([255, 0, 0]))

        # Animate the thing
        self.carx += 0.1
        self.tirez += -2


if __name__ == "__main__":
    Lab6Renderer.run()
