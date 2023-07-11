from PIL import Image


def mix1(img, img2):
    w, h = img.size

    newImage = Image.new("RGB", (w, h))

    for i in range(1, w-1):
        for j in range(1, h-1):
            r, g, b = img.getpixel((i, j))
            r2, g2, b2 = img2.getpixel((i, j))

            newImage.putpixel((i, j), (r + r2, g + g2, b + b2))

    return newImage


def mix2(img1, img2, alpha=0.5):
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')

    pixels1 = img1.load()
    pixels2 = img2.load()

    mixed_img = Image.new('RGBA', img1.size)

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r1, g1, b1, a1 = pixels1[i, j]
            r2, g2, b2, a2 = pixels2[i, j]

            r = int(r1 * alpha + r2 * (1 - alpha))
            g = int(g1 * alpha + g2 * (1 - alpha))
            b = int(b1 * alpha + b2 * (1 - alpha))
            a = int(a1 * alpha + a2 * (1 - alpha))

            mixed_img.putpixel((i, j), (r, g, b, a))

    mixed_img = mixed_img.convert('RGB')

    return mixed_img


def mix3(image, second_image):
    result_img = Image.new('RGB', (image.width, image.height))
    w, h = image.size

    for i in range(w):
        for j in range(h):
            r_a, g_a, b_a = image.getpixel((i, j))
            r_b, g_b, b_b = second_image.getpixel((i, j))

            r = int((2*(r_a / 255)*(r_b / 255) if ((r_b / 255) < 0.5) else 1 - 2*(1 - (r_a / 255))*(1 - (r_b / 255))) * 255.999)
            g = int((2*(g_a / 255)*(g_b / 255) if ((g_b / 255) < 0.5) else 1 - 2*(1 - (g_a / 255))*(1 - (g_b / 255))) * 255.999)
            b = int((2*(b_a / 255)*(b_b / 255) if ((b_b / 255) < 0.5) else 1 - 2*(1 - (b_a / 255))*(1 - (b_b / 255))) * 255.999)

            result_img.putpixel((i, j), (r, g, b))

    return result_img


def mix4(img1, img2):
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')

    pixels1 = img1.load()
    pixels2 = img2.load()

    mixed_img = Image.new('RGBA', img1.size)

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r1, g1, b1, a1 = pixels1[i, j]
            r2, g2, b2, a2 = pixels2[i, j]

            r = int(r1 * (r2 / 255))
            g = int(g1 * (g2 / 255))
            b = int(b1 * (b2 / 255))
            a = int(a1 * a2 / 255)

            mixed_img.putpixel((i, j), (r, g, b, a))

    mixed_img = mixed_img.convert('RGB')

    return mixed_img


def mix5(img1, img2):
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')

    pixels1 = img1.load()
    pixels2 = img2.load()

    mixed_img = Image.new('RGBA', img1.size)

    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r1, g1, b1, a1 = pixels1[i, j]
            r2, g2, b2, a2 = pixels2[i, j]

            r = int(255 - (255 - r1) * (255 - r2) / 255)
            g = int(255 - (255 - g1) * (255 - g2) / 255)
            b = int(255 - (255 - b1) * (255 - b2) / 255)
            a = int(a1 * a2 / 255)

            mixed_img.putpixel((i, j), (r, g, b, a))

    mixed_img = mixed_img.convert('RGB')

    return mixed_img

def mix6(img1, img2):
    # konwersja obrazów do trybu RGBA (z kanałem przezroczystości)
    img1 = img1.convert('RGBA')
    img2 = img2.convert('RGBA')

    # pobieranie tablic pikseli obu obrazów
    pixels1 = img1.load()
    pixels2 = img2.load()

    # tworzenie nowego obrazu w trybie RGBA
    mixed_img = Image.new('RGBA', img1.size)

    # mieszanie pikseli obu obrazów
    for i in range(img1.size[0]):
        for j in range(img1.size[1]):
            r1, g1, b1, a1 = pixels1[i, j]
            r2, g2, b2, a2 = pixels2[i, j]

            # obliczanie nowych wartości kolorów i przezroczystości piksela
            r = min(r1, r2)
            g = min(g1, g2)
            b = min(b1, b2)
            a = int((a1 + a2) / 2)

            # zapisywanie piksela do nowego obrazu
            mixed_img.putpixel((i, j), (r, g, b, a))

    # konwersja obrazu do trybu RGB (bez kanału przezroczystości)
    mixed_img = mixed_img.convert('RGB')

    # zwracanie wyniku
    return mixed_img
