from typing import List

import tensorflow as tf
import cv2

from DifferenceLocator import DifferenceLocator


def log_tensor(tensor):
    tf.print(tensor, summarize=tf.size(tensor),
             output_stream="file://log.txt")


def check_difference_location(tensor, equality) -> []:
    difference_locators = []
    np_array = tensor.numpy()
    if not equality:
        for row in range(np_array.shape[0]):
            for pixel in range(np_array.shape[1]):
                if any(np_array[row, pixel] == 0):
                    dl = DifferenceLocator()
                    dl.set_row(row)
                    dl.set_pixel(pixel)
                    difference_locators.append(dl)
    return difference_locators


def define_differences(image_downloaded, difference_locators: List[DifferenceLocator]):
    img = cv2.imread(image_downloaded)

    for obj in difference_locators:
        row = obj.get_row()
        pixel = obj.get_pixel()
        cv2.circle(img, (pixel, row), radius=2, color=(0, 0, 255), thickness=-1)

    cv2.imshow('Marked Image', img)
    cv2.waitKey(1)
    # cv2.imwrite('control/negative.jpg', img)
    ...
