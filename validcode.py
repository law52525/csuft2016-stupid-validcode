import os
import requests
from PIL import Image


def get_valid_code(n):
    for i in range(n):
        r = requests.get("http://222.22.224.8:8080/eportal/validcode").content
        with open("img/{}.png".format(i), "wb") as f:
            f.write(r)


def binary_and_crop():
    path = 'img/'
    for i in os.listdir(path):
        img = Image.open(path + i)
        img = img.convert('L')
        img = img.point(lambda x: 0 if x > 200 else 1, '1')
        img.save(path + i)
        y_min, y_max = 5, 25
        split_lines = [10, 25, 40, 55, 70]
        imgs = [img.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
        for j, v in enumerate(imgs):
            v.save('split_img/{}_{}.png'.format(i, j))


if __name__ == '__main__':
    get_valid_code(50)
    binary_and_crop()
