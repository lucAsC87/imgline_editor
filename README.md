# imgline_editor
#### Video Demo:  <https://www.youtube.com/watch?v=84V9ymQ26YY>
#### Description:
imgline_editor was built to provide a simple image editor that can be used directly from the terminal.

It uses the modules Image and ImageOps from Pillow to handle the images and the library sys to handle the command-line arguments.

All the functionalities are managed by four functions:

- helper: if called with the flag -h, this function prints a help message to the user to explain to him how to use the program

- arguments_checker: checks if the arguments passed to the program are too few or too many and, just in case, close the program using sys.exit and suggesting the user how to call the helper function

- format_checker: checks that the file to edit is between allowed image formats. Otherwise, close the program using sys.exit and print to the user that the image format was invalid.

- editor: the core of the program, where the magic happens. First of all, creates a list with all the arguments passed by the user. Then checks if between the arguments there are some flags that perform some of the possible edit operations, like:
    -f, to flip the image vertically (using ImageOps.flip())
    -i, to invert the image colors (using ImageOps.invert())
    -m, to flip the image horizontally (using ImageOps.mirror())
    -g, to convert the image to grayscale (using ImageOps.grayscale())
Then, it returns the edited image.

Inside the main function, after helper() and arguments_checker(), there is a variable "name" assigned to last sys.argv (namely, the image file to edit). After checking if the file is in an appropriate format using format_checker it performs a try/except block, trying to open the file with Image.open() or closing the program with sys.exit in case the file does not exist. Then, it calls the editor() function on the opened file and save that with Image.save(), adding to its name "edited_" at the beginning. It then prints a confirmation message to the user that the file has been edited.
That's it!
