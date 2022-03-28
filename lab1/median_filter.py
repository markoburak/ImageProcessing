import random

import numpy
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from skimage.util import random_noise


def add_noise(img):
    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img


def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = numpy.zeros((len(data), len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def main():
    filename = "apple"
    kernel = 3
    dir_salt = "detailed_salt"
    dir_denoised = "detailed_denoised"
    img = cv2.imread(filename+".jpg", cv2.IMREAD_GRAYSCALE)
    noisy_gray = add_noise(img)
    cv2.imwrite(f'{dir_salt}/salt-and-pepper-{filename}-{kernel}.jpg', img)

    arr = numpy.array(noisy_gray)
    removed_noise = median_filter(arr, kernel)
    cv2.imwrite(f"{dir_denoised}/image-denoised-{filename}-{kernel}.jpg", removed_noise)


if __name__ == "__main__":
    main()
