import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    for i in range(185, 295):
        for j in range(520, 570):
            if data[i, j] < 170 and data[i, j] > 50:
                hit('down')
                return

    for i in range(190, 430):
        for j in range(655, 675):
            if data[i, j] < 170 and data[i, j] > 50:
                hit('up')
                return


if __name__ == "__main__":
    print("Game will start in 3 seconds")
    time.sleep(1)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # Draw the rectangle for cactus
        # for i in range(190, 410):
        #     for j in range(655, 675):
        #         data[i, j] = 170
        #
        # # Draw the rectangle for bird
        # for i in range(185, 300):
        #     for j in range(520, 570):
        #         data[i, j] = 0
        # image.show()
        # break
