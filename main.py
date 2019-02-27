import tensorflow as tf
import numpy as np
import requests
from PIL import Image


def get_img():
    r = requests.get("http://222.22.224.8:8080/eportal/validcode").content
    with open("tmp.png", "wb") as f:
        f.write(r)


def pre_treat_img():
    img = Image.open("tmp.png").convert('L')  # 灰度
    img = img.point(lambda x: 0 if x > 200 else 1, '1')  # 二值化

    # 切割
    y_min, y_max = 5, 25
    split_lines = [10, 25, 40, 55, 70]
    imgs = [img.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
    return imgs


if __name__ == '__main__':
    get_img()
    code = np.zeros(shape=(4, 20, 15), dtype=np.float32)
    num = []
    model = tf.keras.models.load_model('my_model.h5')
    for i, v in enumerate(pre_treat_img()):
        code[i] += np.asarray(v, dtype=np.float32)
    for v in model.predict(code).argmax(axis=1):
        num.append(str(v))
    print(''.join(num))
    Image.open("tmp.png").show()
