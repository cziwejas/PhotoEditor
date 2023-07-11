from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def negatyw(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            r, g, b = img.getpixel((i, j))
            result_img.putpixel((i, j), (255 - r, 255 - g, 255 - b))

    return result_img
