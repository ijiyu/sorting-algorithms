from PIL import Image, ImageDraw
import random
import os
import glob
import subprocess

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
BACKGROUND_COLOR = "#000000"
DEFAULT_COLOR = "#ffffff"
SELECTED_COLOR = "#ff0000"
FINISHED_COLOR = "#00ff00"
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


def draw_bars(bars, filename, dir):
    image = Image.new("RGB", (SCREEN_WIDTH, SCREEN_HEIGHT), BACKGROUND_COLOR)
    canvas = ImageDraw.Draw(image)
    for bar in bars:
        bar.draw(canvas)
    image.save(os.path.join(dir, filename))


def initialize(x_positions, heights, bars):
    x_positions = list(range(0, SCREEN_WIDTH, BAR_WIDTH))
    heights = [(x_position+BAR_WIDTH)*0.5 for x_position in x_positions]
    random.shuffle(heights)

    bars = [
        Bar(BAR_WIDTH, h, x, DEFAULT_COLOR, BAR_XPADDING)
        for x, h in zip(x_positions, heights)
    ]


def prepare_folder(dir):
    os.makedirs(dir, exist_ok=True)
    for file_path in glob.glob(os.path.join(dir, "*")):
        if os.path.isfile(file_path):
            os.remove(file_path)


def finish(bars):
    for bar in bars:
        bars.color = FINISHED_COLOR
        draw_bars(bars, f"{frame}.jpg")
        frame += 1


def bubble_sort():
    x_positions, heights, bars = None
    initialize(x_positions, heights, bars)

    frame = 0
    output_dir = "frames"

    prepare_folder(output_dir)
    draw_bars(bars, "0.jpg")

    for _ in range(len(bars)-1):
        done = True
        for i in range(len(bars)-1):
            bars[i].color, bars[i+1].color = SELECTED_COLOR, SELECTED_COLOR
            if bars[i].height > bars[i+1].height:
                bars[i].height, bars[i+1].height = bars[i+1].height, bars[i].height
                done = False
            draw_bars(bars, f"{frame}.jpg", output_dir)

            frame += 1
            bars[i].color, bars[i+1].color = DEFAULT_COLOR, DEFAULT_COLOR
        if done:
            break

    finish(bars)


def build_video():
    subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", "build_video.ps1"],
        check=True
    )


def main():
    bubble_sort()
    build_video()


if __name__ == "__main__":
    main()
