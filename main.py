from PIL import Image, ImageDraw
import random

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
BACKGROUND_COLOR = "#000000"
BAR_COLOR = "#ffffff"
BAR_WIDTH = 40
BAR_XPADDING = 5


class Bar:
    def __init__(self, width, height, x, color, xpadding):
        self.width = width
        self.height = height
        self.x = x
        self.color = color
        self.xpadding = xpadding

    def draw(self, canvas):
        shape = [
            (self.x + self.xpadding, SCREEN_HEIGHT - self.height),
            (self.x + self.width - self.xpadding, SCREEN_HEIGHT)
        ]
        canvas.rectangle(shape, fill=self.color)


def main():
    x_positions = list(range(0, SCREEN_WIDTH, BAR_WIDTH))
    heights = [(x_position+BAR_WIDTH)*0.5 for x_position in x_positions]
    random.shuffle(heights)

    bars = [
        Bar(BAR_WIDTH, h, x, BAR_COLOR, BAR_XPADDING)
        for x, h in zip(x_positions, heights)
    ]

    random.shuffle(bars)

    image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), BACKGROUND_COLOR)
    canvas = ImageDraw.Draw(image)

    for bar in bars:
        bar.draw(canvas)

    image.show()


if __name__ == "__main__":
    main()
