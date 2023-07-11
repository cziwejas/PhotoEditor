from PIL import Image


def kontrast(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            r = (r - 128) * 2 + 128
            g = (g - 128) * 2 + 128
            b = (b - 128) * 2 + 128
            result_img.putpixel((i, j), (r, g, b))

    return result_img
