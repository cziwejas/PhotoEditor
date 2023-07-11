from PIL import Image


def potegowa(img, n):
    n = float(n)
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            r, g, b = img.getpixel((i, j))
            temp_r = int(pow(r/255.0, n) * 255)
            temp_g = int(pow(g/255.0, n) * 255)
            temp_b = int(pow(b/255.0, n) * 255)
            result_img.putpixel((i, j), (temp_r, temp_g, temp_b))

    return result_img
