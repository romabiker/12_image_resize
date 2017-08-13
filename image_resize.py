from PIL import Image
import argparse
import os
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--width', type=int,
                        help='desired width of the image')
    parser.add_argument('-ht', '--height', type=int,
                        help='desired height of the image')
    parser.add_argument('-s', '--scale', type=float,
                        help='desired scale to transform the image')
    parser.add_argument('-op', '--outpath', type=str,
                        help='path to save new image')
    parser.add_argument('-if', '--infile', type=argparse.FileType(mode='rb'),
                        required=True, help='path to the image for resize')
    return parser


def is_new_image_proportional(width, height, image):
    return round(width / height) == round(image.width / image.height)


def resize_image(width, height, scale, inimage_file):
    image = Image.open(inimage_file)
    if scale:
        height = round(scale * image.height)
        width = round(scale * image.width)
    if not height:
        height = round(width / image.width * image.height)
    if not width:
        width = round(image.height / height * image.width)
    if not is_new_image_proportional(width, height, image):
        print_not_original_proportions_warning_to_console()
    return image.resize((width, height))


def print_not_original_proportions_warning_to_console():
    print('New image proportions are not the same as the original')


def save_new_image(new_image, inimage_file, outpath):
    if not outpath:
        name, extension = os.path.splitext(inimage_file.name)
        outpath = '{}__{}x{}{}'.format(name, new_image.width,
                                       new_image.height, extension)
    new_image.save(outpath)


def isvalid_namespace(namespace):
    if not any((
            namespace.width,
            namespace.height,
            namespace.scale
            )):
        print('You have to provide width or height or scale')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if not isvalid_namespace(namespace):
        sys.exit()
    new_image = resize_image(
                namespace.width,
                namespace.height,
                namespace.scale,
                namespace.infile
                )
    save_new_image(new_image, namespace.infile, namespace.outpath)
