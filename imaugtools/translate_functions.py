import cv2
import numpy as np


def translate_image(image, tx: int, ty: int, tx_max=None, ty_max=None, crop=True):

    # arguments
    # tx_max: max translation window size on left and right
    # ty_max: max translation window size on top and bottom
    # tx: can vary from 0 to tx_max
    # ty: can vary from 0 to ty_max
    # crop: can be false when tx and ty are not specified

    if not crop and ty_max is not None and tx_max is not None:
        raise ValueError("Can't have crop=False when tx_max or ty_max is specified")
    if tx_max is None: tx_max = abs(tx)
    if ty_max is None: ty_max = abs(ty)

    # predict the size from tx_max and ty_max and resize
    size = (int(image.shape[0] / (1 + 2 * ty_max)), int(image.shape[1] / (1 + 2 * tx_max)))

    # get offsets for centered image
    top_offset = int((image.shape[0] - size[0]) // 2)
    left_offset = int((image.shape[1] - size[1]) // 2)

    # calculate new offsets based on tx and ty
    top_offset = top_offset + int(size[0] * ty)
    left_offset = left_offset + int(size[1] * tx)

    if top_offset < 0 or left_offset < 0 or \
            top_offset + size[0] > image.shape[0] \
            or left_offset + size[1] > image.shape[1]:
        print('Image Shape: ', image.shape)
        print('Crop: ', [top_offset, top_offset + size[0], left_offset, left_offset + size[1]])
        raise ValueError('Could not crop image')

    if not crop:
        tx *= -1
        uncropped_image = np.zeros(image.shape, dtype='uint8')

        if ty > 0: top_offset_u = 0
        else: top_offset_u = image.shape[0] - size[0]

        if tx > 0: left_offset_u = 0
        else: left_offset_u = image.shape[1] - size[1]

        uncropped_image[top_offset_u:top_offset_u + size[0], left_offset_u:left_offset_u + size[1]] = image[top_offset:top_offset + size[0], left_offset:left_offset + size[1]]
        return uncropped_image
    return image[top_offset:top_offset + size[0], left_offset:left_offset + size[1]]
