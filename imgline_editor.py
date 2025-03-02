#!/usr/bin/env python

from PIL import Image, ImageOps
import sys


def main():
    helper(sys.argv)
    arguments_checker(sys.argv)
    # assign name to the last argument
    name = sys.argv[len(sys.argv) - 1]
    format_checker(name)
    # try to open the image, otherwise close the program
    try:
        file_img = Image.open(name)
    except FileNotFoundError:
        sys.exit("The requested file does not exist.")
    file_img = editor(sys.argv, file_img).save("edited_" + name)
    print("Image edited")


# print help message if requested
def helper(lst):
    help_message = "Type ./imgline_editor.py -FLAG(S) IMAGE to edit the image\n Available flags:\n -f flip the image vertically\n -i invert the image colors\n -m flip the image orizontally\n -g convert the image to grayscale"
    if len(lst) == 2 and lst[1] == "-h":
        sys.exit(help_message)


# check for the appropriate number of command-line arguments
def arguments_checker(lst):
    if len(lst) < 3:
        sys.exit("Too few command-line arguments. Type ./imgline_editor.py -h for help.")
    if len(lst) > 6:
        sys.exit("Too many command-line arguments. Type ./imgline_editor.py -h for help.")


# check the file format
def format_checker(f_name):
    file_name = f_name.strip().lower().split(".")
    file_format = file_name[len(file_name) - 1]
    images_format = (
        "apng",
        "avif",
        "bmp",
        "gif",
        "ico",
        "jpeg",
        "jpg",
        "png",
        "svg",
        "tif",
        "tiff",
        "webp",
    )
    if file_format not in images_format:
        sys.exit("Invalid image format")


# edit the image based on the flags
def editor(lst, img):
    commands = list()
    # create list of commands
    for command in lst:
        commands.append(command)
    # flip the image vertically
    if "-f" in commands:
        img = ImageOps.flip(img)
    # invert the colors of the image
    if "-i" in commands:
        img = ImageOps.invert(img)
    # flip the image horizontally
    if "-m" in commands:
        img = ImageOps.mirror(img)
    # convert the image to grayscale
    if "-g" in commands:
        img = ImageOps.grayscale(img)
    return img


if __name__ == "__main__":
    main()
