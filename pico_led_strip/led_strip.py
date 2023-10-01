from neopixel import Neopixel
from LEDArray import LEDArray, ColorPalette, PaletteRoll, Sparkle
import time

NUM_PIXELS = 100
PORT = 28
STATE_MACHINE = 0
DELAY = 0.001
MODE = "GRB"
BRIGHTNESS = 10

strip = Neopixel(NUM_PIXELS, STATE_MACHINE, PORT, MODE, DELAY)
strip.brightness(BRIGHTNESS)

led_array = LEDArray(strip)
strip.clear()

from palettes import fire, white_to_black
fire_palette = ColorPalette(fire, NUM_PIXELS)
sparkle_palette = ColorPalette(white_to_black, 24)
trans_palette_roll = PaletteRoll(led_array, fire_palette, 1)
trans_sparkle = Sparkle(led_array, sparkle_palette, 1)
transforms = [
    trans_palette_roll,
    trans_sparkle
]
led_array.assign_transforms(transforms)

while True:
    led_array.update_array()

