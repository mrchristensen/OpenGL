from gl_base import Renderer
import numpy as np


class Lab5Renderer(Renderer):
    title = "Lab 5: 3D Rendering (OpenGL)"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def poll_keys(self):
        """Handles key press events
        TODO: insert key press event code here:
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
        if self.key_pressed[self.keys.A]:
            print("A is pressed")

    def get_projection(self):
        """gets the projection matrix
        TODO: if in p state, returns perspective matrix
        TODO: if in o state, returns orthographic matrix
        """
        return np.eye(4)

    def get_view(self):
        """gets the view matrix
        TODO: return the view matrix
        """
        return np.eye(4)


if __name__ == "__main__":
    Lab5Renderer.run()
