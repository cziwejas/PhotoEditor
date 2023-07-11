import matplotlib.pyplot as plt


def histogram(img):
    w, h = img.size

    r_list = []
    g_list = []
    b_list = []

    for i in range(1, w-1):
        for j in range(1, h-1):
            r, g, b = img.getpixel((i,j))

            r_list.append(r)
            g_list.append(g)
            b_list.append(b)

    fig, axs = plt.subplots(1, 3, figsize=(10, 5))

    axs[0].hist(r_list, bins=256, range=(0, 255), color='r', alpha=0.5)
    axs[0].set_title('Kanał R')

    axs[1].hist(g_list, bins=256, range=(0, 255), color='g', alpha=0.5)
    axs[1].set_title('Kanał G')

    axs[2].hist(b_list, bins=256, range=(0, 255), color='b', alpha=0.5)
    axs[2].set_title('Kanał B')

    plt.show()