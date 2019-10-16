import cv2


def center_crop(image, size):
    # find larger ratio
    h_ratio = size[0] / image.shape[0]
    w_ratio = size[1] / image.shape[1]
    larger_ratio = h_ratio if h_ratio > w_ratio else w_ratio

    # resize with larger ratio
    image = cv2.resize(image, (0, 0), fx=larger_ratio, fy=larger_ratio)

    # crop the middle portion
    top_offset = (image.shape[0] - size[0]) // 2
    left_offset = (image.shape[1] - size[1]) // 2

    image = image[top_offset:top_offset + size[0], left_offset:left_offset + size[1]]

    return image


def crop_around_center(image, width, height):
    """
    Given a NumPy / OpenCV 2 image, crops it to the given width and height,
    around it's centre point
    """

    image_size = (image.shape[1], image.shape[0])
    image_center = (int(image_size[0] * 0.5), int(image_size[1] * 0.5))

    if width > image_size[0]:
        width = image_size[0]

    if height > image_size[1]:
        height = image_size[1]

    x1 = int(image_center[0] - width * 0.5)
    x2 = int(image_center[0] + width * 0.5)
    y1 = int(image_center[1] - height * 0.5)
    y2 = int(image_center[1] + height * 0.5)

    return image[y1:y2, x1:x2]
