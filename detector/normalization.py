#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@ScriptName  : normalization.py
@Project     : Object-Detection-Cascades
@Author      : Meng Peng
@Date        : 08-08-2020
@Description : normalize all positive and negative samples
"""
import os
import glob
from PIL import Image


def normalization(img_file, save_dir, positive=True, width=24, height=24):
    img = Image.open(img_file)
    print(img)
    try:
        if not positive:
            width = img.size[0]
            height = img.size[1]

        new_img_tmp = img.resize((width, height), Image.BILINEAR)
        new_img = new_img_tmp.convert('L')
        print(new_img)
        new_img.save(os.path.join(save_dir, os.path.basename(img_file)))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    base_path = os.path.abspath("..")
    img_pos = base_path + '/resource/positive_samples/positive/*.bmp'
    img_neg = base_path + '/resource/negative_samples/negative/*.bmp'
    pos_dir = base_path + '/detector/data/pos'
    neg_dir = base_path + '/detector/data/neg'

    for img_file in glob.glob(img_pos):
        normalization(img_file, pos_dir)

    for img_file in glob.glob(img_neg):
        normalization(img_file, neg_dir, False)
