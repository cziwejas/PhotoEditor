from PIL import Image


def roberts(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[0, 0, 0], [0, 1, -1], [0, 0, 0]]

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def roberts2(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[0, 0, 0], [0, 1, 0], [0, -1, 0]]

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def prewitt(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]] # Prewitt

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def prewitt2(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[1, 0, -1], [1, 0, -1], [1, 0, -1]] # Prewitt

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def sobel(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]  # Sobel

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def sobel2(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]  # Sobel

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def laplace(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[-2, 1, -2], [1, 4, 1], [-2, 1, -2]] # Laplaca

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img


def laplace2(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    maska = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]  # Laplaca

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            tmp_r = 0
            tmp_g = 0
            tmp_b = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    tmp_r += r * maska[x + 1][y + 1]
                    tmp_g += g * maska[x + 1][y + 1]
                    tmp_b += b * maska[x + 1][y + 1]
            result_img.putpixel((i, j), (tmp_r, tmp_g, tmp_b))

    return result_img