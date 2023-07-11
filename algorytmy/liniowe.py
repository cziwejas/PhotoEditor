from PIL import Image


def rozjasnienie(img):
    result_img = Image.new('RGB', (img.width, img.height))
    w, h = img.size

    alpha = 2
    beta = 40

    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            r = int(alpha * r + beta)
            g = int(alpha * g + beta)
            b = int(alpha * b + beta)
            result_img.putpixel((i, j), (r, g, b))

    return result_img


def przyciemnienie(img):
    result_img = Image.new('RGB', (img.width, img.height))
    w, h = img.size

    alpha = 0.50
    beta = 2

    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            r = int(alpha * r + beta)
            g = int(alpha * g + beta)
            b = int(alpha * b + beta)
            result_img.putpixel((i, j), (r, g, b))

    return result_img