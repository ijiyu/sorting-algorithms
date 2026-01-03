from PIL import Image, ImageDraw
import random
import os
import glob

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


def draw_bars(bars, filename):
    output_dir = "frames"
    image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), BACKGROUND_COLOR)
    canvas = ImageDraw.Draw(image)
    for bar in bars:
        bar.draw(canvas)
    image.save(os.path.join(output_dir, filename))


def bubble_sort():
    x_positions = list(range(0, SCREEN_WIDTH, BAR_WIDTH))
    heights = [(x_position+BAR_WIDTH)*0.5 for x_position in x_positions]
    random.shuffle(heights)

    bars = [
        Bar(BAR_WIDTH, h, x, BAR_COLOR, BAR_XPADDING)
        for x, h in zip(x_positions, heights)
    ]

    iteration = 0
    output_dir = "frames"
    os.makedirs(output_dir, exist_ok=True)
    for file_path in glob.glob(os.path.join(output_dir, "*")):
        if os.path.isfile(file_path):
            os.remove(file_path)
    draw_bars(bars, "0.jpg")

    for _ in range(len(bars)-1):
        done = True
        for i in range(len(bars)-1):
            bars[i].color = "#ff0000"
            bars[i+1].color = "#ff0000"
            if bars[i].height > bars[i+1].height:
                bars[i].height, bars[i+1].height = bars[i+1].height, bars[i].height
                done = False
            draw_bars(bars, f"{iteration}.jpg")

            iteration += 1
            bars[i].color = "#ffffff"
            bars[i+1].color = "#ffffff"
        if done:
            break

    for i in range(len(bars)):
        bars[i].color = "#00ff00"
        draw_bars(bars, f"{iteration}.jpg")
        iteration += 1


def main():
    bubble_sort()


if __name__ == "__main__":
    main()
