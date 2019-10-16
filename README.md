# imaugtools

imaugtools contains tools used for image augmentation: translate, rotate, crop. This library is for you if you do NOT want to stretch or skew, or pad pixels that would make your images look strange when doing any of these operations.

## Installation

To install imaugtools, simply run in your terminal
```sh
pip install imaugtools
```

## Usage

Example image

![example-image](example/lenna_small.png)

### Translation

```py
my_image_translated = translate_image(my_image, 0.1, 0.2)
my_image_translated_uncropped = translate_image(my_image, 0.1, 0.2, crop=False)
imshow(my_image_translated, my_image_translated_uncropped, mode='BGR')
```

![translated-image](example/lenna_translated.png)

### Rotation

```py
my_image_rotated = rotate_image(my_image, 30)
my_image_rotated_uncropped = rotate_image(my_image, 30, crop=False)
imshow(my_image_rotated, my_image_rotated_uncropped, mode='BGR')
```

![rotated-image](example/lenna_translated.png)

### Cropping

```py
my_image_center_cropped = center_crop(my_image, (200, 200))
my_image_cropped_around_center = crop_around_center(my_image, 200, 200)
imshow(my_image_center_cropped, my_image_cropped_around_center, mode='BGR')
```

![cropped-image](example/lenna_translated.png)

```py
print(my_image_center_cropped.shape, my_image_cropped_around_center.shape)
# Output: (200, 200, 3) (200, 200, 3)
```

### Note

- Import the above functions from `imaugtools` like,
```py
from imaugtools import translate_image, rotate_image
```
- `imshow` function used here is from [imshowtools](https://github.com/saravanabalagi/imshowtools) library

## Contributing

Pull requests are very welcome.

1. Fork the repo
1. Create new branch with feature name as branch name
1. Check if things work with a jupyter notebook
1. Raise a pull request

## Licence

Please see attached [Licence](LICENSE)