# !/usr/bin/env python

import sys

from PIL import Image


def main() -> None:
    with Image.open(sys.argv[1]) as image:
        image.transpose(Image.TRANSPOSE).save(sys.argv[2])


if __name__ == '__main__':
    main()
