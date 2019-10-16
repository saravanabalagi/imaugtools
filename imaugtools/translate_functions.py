import cv2


def translate_image(image, tx_prime, ty_prime, tx, ty):

    # predict the size from tx_prime and ty_prime and resize
    size = (int(image.shape[0] / (1 + 2 * ty_prime)), int(image.shape[0] / (1 + 2 * tx_prime)))
    image_resized = cv2.resize(image, size)

    # get offsets for centered image
    top_offset = int((image.shape[0] - size[0]) // 2)
    left_offset = int((image.shape[1] - size[1]) // 2)

    # calculate new offsets based on tx and ty
    top_offset = top_offset + int(image_resized.shape[0] * ty)
    left_offset = left_offset + int(image_resized.shape[1] * tx)

    if top_offset < 0 or left_offset < 0 or \
            top_offset + size[0] > image.shape[0] \
            or left_offset + size[1] > image.shape[1]:
        print('Image Shape: ', image.shape)
        print('Crop: ', [top_offset, top_offset + size[0], left_offset, left_offset + size[1]])
        raise ValueError('Could not crop image')

    return image[top_offset:top_offset + size[0], left_offset:left_offset + size[1]]
