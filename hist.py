# !/usr/bin/env python

import sys
from collections import defaultdict

from PIL import Image


def hist(image: Image):
    rgb_image = image.convert('RGB')
    color_count_dict = defaultdict(int)
    width, height = image.size

    for pixel in zip(range(width), range(height)):
        color_count_dict[rgb_image.getpixel(pixel)] += 1
    return color_count_dict


def main():
    with Image.open(sys.argv[1]) as image:
        for rgb_pixel, count in sorted(hist(image).items(),
                                       key=lambda kv: kv[1],
                                       reverse=True):
            print(*rgb_pixel, sep=', ', end=': ')
            print(count)


if __name__ == '__main__':
    main()
