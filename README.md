# Image Resizer

The script resizes the given image. It requires the path to the original picture, one of the three arguments: new width, height or scale. If width and height were specified both the warning can appear in the console if the proportions do not match the source image. If no path was specified where place the final file, the result would be placed near the source file with the original name plus width and height in its new name.  

## Quickstart

Example of script launch on Linux, Python 3.5:

```
$ pip install -r requirements.txt # alternatively try pip3
$ python3 image_resize.py -s 2 -if image.jpeg

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
