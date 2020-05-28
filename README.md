# imaugtools

![](https://img.shields.io/pypi/v/imaugtools)
![](https://img.shields.io/pypi/wheel/imaugtools)
![](https://img.shields.io/pypi/l/imaugtools)
![](https://img.shields.io/pypi/dm/imshowtools)

imaugtools contains tools used for image augmentation: translate, rotate, crop. This library is for you if you do NOT want to stretch or skew, or pad pixels that would make your images look strange when doing any of these operations.

## Installation

To install imaugtools, simply run in your terminal
```sh
pip install imaugtools
```

## Usage

Example image

![example-image](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_small.png)

### Translation

```py
from imaugtools import translate_image
my_image_translated = translate_image(my_image, 0.1, 0.2)
my_image_translated_uncropped = translate_image(my_image, 0.1, 0.2, crop=False)
imshow(my_image_translated, my_image_translated_uncropped, mode='BGR')
```
`imshow` function used here is to simply display the images, you can use it from [imshowtools](https://github.com/saravanabalagi/imshowtools) library.

With and without crop:

![translated-image](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_translated.png)

### Rotation

```py
from imaugtools import rotate_image
my_image_rotated = rotate_image(my_image, 30) # angle in degrees
my_image_rotated_uncropped = rotate_image(my_image, 30, crop=False)
imshow(my_image_rotated, my_image_rotated_uncropped, mode='BGR')
```
With and without crop:

![rotated-image](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_rotated.png)

### Cropping

```py
from imaugtools import center_crop, crop_around_center
my_image_center_cropped = center_crop(my_image, (150, 200))
my_image_cropped_around_center = crop_around_center(my_image, (150, 200))
imshow(my_image_center_cropped, my_image_cropped_around_center, mode='BGR')
```

Aspect ratio preserving center crop and crop around center:

![cropped-image](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_cropped.png)

```py
print(my_image_center_cropped.shape, my_image_cropped_around_center.shape)
# Output: (200, 200, 3) (200, 200, 3)
```

## Advanced Usage

### Strided Translation

Strided translation is very powerful image augmentation techniques used in training neural networks.

`tx_max = 1` and `ty_max = 1` is equivalent to a stride of 1 in both directions. After you specify `tx_max`, you can specify `tx` (translation in x-axis) from -`tx_max` to +`tx_max`. The same applies to `ty` and `ty_max`.

```py
my_images_translated = []
for j in range(-1, 2):
    for i in range(-1, 2):
        my_images_translated.append(translate_image(my_image, i, j, tx_max=1, ty_max=1))
imshow(*my_images_translated, mode='BGR')
```
![stride-1-translation](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_stride_1.png)



`tx_max = 0.5` and `ty_max = 0.5` is equivalent to a stride of 0.5 in both directions

```py
my_images_translated = []
for j in range(-2, 3):
    for i in range(-2, 3):
        my_images_translated.append(translate_image(my_image, i/4, j/4, tx_max=0.5, ty_max=0.5))
imshow(*my_images_translated, mode='BGR')
```
![stride-0.5-translation](https://github.com/saravanabalagi/imaugtools/raw/master/example/lenna_stride_0.5.png)


## Contributing

Pull requests are very welcome.

1. Fork the repo
1. Create new branch with feature name as branch name
1. Check if things work with a jupyter notebook
1. Raise a pull request

## Licence

Please see attached [Licence](LICENSE)
