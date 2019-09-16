# coding=utf-8

import os
import numpy as np
import cv2

img_path = '/nfs/cold_project/yzh/baidu/dataset/baidu_train/bbox_more_voc/JPEGImages/'

R_means = list()
G_means = list()
B_means = list()

for pic in os.listdir(img_path):
    pic_path = os.path.join(img_path, pic)
    img = cv2.imread(pic_path)
    im_R = img[:, :, 0]
    im_G = img[:, :, 1]
    im_B = img[:, :, 2]

    im_R_mean = np.mean(im_R)
    im_G_mean = np.mean(im_G)
    im_B_mean = np.mean(im_B)

    R_means.append(im_R_mean)
    G_means.append(im_G_mean)
    B_means.append(im_B_mean)

a = [R_means, G_means, B_means]
mean = [0,0,0]

mean[0] = np.mean(a[0])
mean[1] = np.mean(a[1])
mean[2] = np.mean(a[2])

print("RGB means:\n [{}, {}, {}]".format(mean[2], mean[1], mean[0]))



