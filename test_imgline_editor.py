from imgline_editor import helper, arguments_checker, format_checker, editor
from PIL import Image
import pytest


def test_helper():
    test_list = ("program", "-h")
    with pytest.raises(SystemExit):
        helper(test_list)


def test_import_arguments():
    test_short_list = ("one", "two")
    test_long_list = ("one", "two", "three", "four", "five", "six", "seven")
    with pytest.raises(SystemExit):
        arguments_checker(test_short_list)
        arguments_checker(test_long_list)


def test_format_checker():
    with pytest.raises(SystemExit):
        format_checker("test.txt")
        format_checker("test.avi")
        format_checker("test.pdf")


def test_editor():
    test_list = ("-b", "-n", "-s")
    img = Image.open("test_image.png")
    assert editor(test_list, img) == img
