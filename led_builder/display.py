from mapping import LinearTo2DArray
from neopixel import Neopixel

class Frame2D:
    def __init__(self, numpixels, width):
        self.pixels = [0]*numpixels
        self.map = LinearTo2DArray(numpixels, width)

    def get_val(self, idx):
        return self.pixels[idx]

    def set_val(self, x, y, color, brightness=None):
        idx = self.map.map_2D_linear(x, y)
        self.pixels[idx] = color, brightness

# class Frames(list):
#     pass

class Display2D:
    def __init__(self, numpixels, width, sm, port, mode, delay):
        self.idx_pixels = range(numpixels)
        self.width = width
        self.strip = Neopixel(numpixels, sm, port, mode, delay)

    def set_frames(self, frames):
        self.frames = frames
        
    def update(self):
        for frame in self.frames:
            for pixel in self.idx_pixels:
                self.strip.set_pixel(*frame.get_val(pixel))
            self.strip.show()

    def clear(self):
        self.strip.clear()
