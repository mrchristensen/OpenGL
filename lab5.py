from gl_base import Renderer
import numpy as np


class Lab5Renderer(Renderer):
    title = "Lab 5: 3D Rendering (OpenGL)"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cx = 0
        self.cy = 0
        self.cz = -20
        self.theta = 0
        self.perspective = 1

    def poll_keys(self):
        """Handles key press events
        a: move left
        d: move right
        s: move back
        w: move forward
        q: turn left
        e: turn right
        r: move up
        f: move down
        p: change to perspective mode
        o: change to orthographic mode
        h: return "home"
        """
        if self.key_pressed[self.keys.A]:  # Move left
            print("a is pressed")
            self.cx += -np.cos(self.theta)
            self.cz += -np.sin(self.theta)
        elif self.key_pressed[self.keys.D]:  # Move right
            print("d is pressed")
            self.cx += np.cos(self.theta)
            self.cz += np.sin(self.theta)
        elif self.key_pressed[self.keys.S]:  # Move back
            print("s is pressed")
            self.cz += -np.sin(self.theta + (np.pi / 2))
            self.cx += -np.cos(self.theta + (np.pi / 2))
        elif self.key_pressed[self.keys.W]:  # Move forward
            print("w is pressed")
            self.cz += np.sin(self.theta + (np.pi / 2))
            self.cx += np.cos(self.theta + (np.pi / 2))
        elif self.key_pressed[self.keys.Q]:  # Turn left
            print("q is pressed")
            self.theta += 0.1
        elif self.key_pressed[self.keys.E]:  # Turn right
            print("e is pressed")
            self.theta += -0.1
        elif self.key_pressed[self.keys.R]:  # Move up
            print("r is pressed")
            self.cy += 1
        elif self.key_pressed[self.keys.F]:  # Move down
            print("f is pressed")
            self.cy += -1
        elif self.key_pressed[self.keys.P]:  # Change to perspective mode
            print("p is pressed")
            self.perspective = 1
        elif self.key_pressed[self.keys.O]:  # Change to orthographic mode
            print("o is pressed")
            self.perspective = 0
        elif self.key_pressed[self.keys.H]:  # Return home
            self.cx = 0
            self.cy = 0
            self.cz = -20

            self.theta = 0

            print("h is pressed")

    def get_projection(self):
        """gets the projection matrix
        TODO: if in p state, returns perspective matrix
        TODO: if in o state, returns orthographic matrix
        """

        if self.perspective == 1:
            return np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ]).T

        else:
            return np.array([
                [0.1, 0, 0, 0],
                [0, 0.1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]
            ]).T

    def get_view(self):
        """gets the view matrix
        """
        translation = np.array([
            [1, 0, 0, -self.cx],
            [0, 1, 0, -self.cy],
            [0, 0, 1, -self.cz],
            [0, 0, 0, 1]
        ]).T

        rotation = np.array([
            [np.cos(self.theta), 0, np.sin(self.theta), 0],
            [0, 1, 0, 0],
            [-np.sin(self.theta), 0, np.cos(self.theta), 0],
            [0, 0, 0, 1]
        ]).T

        return np.matmul(translation, rotation)


if __name__ == "__main__":
    Lab5Renderer.run()
