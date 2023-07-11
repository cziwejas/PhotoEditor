from PIL import Image


def medianFilter(img):
    result_img = Image.new("RGB", (img.width, img.height))

    w, h = img.size

    for i in range(1, w - 1):
        for j in range(1, h - 1):
            temp_r_list = []
            temp_g_list = []
            temp_b_list = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    r, g, b = img.getpixel((x + i, y + j))
                    temp_r_list.append(r)
                    temp_g_list.append(g)
                    temp_b_list.append(b)

            temp_r_list.sort()
            temp_g_list.sort()
            temp_b_list.sort()

            result_img.putpixel((i, j), (temp_r_list[4], temp_g_list[4], temp_b_list[4]))

    return result_img