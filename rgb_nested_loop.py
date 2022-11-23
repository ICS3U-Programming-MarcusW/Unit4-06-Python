#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Nov 14 2022
# This program uses nested loops to print out all the valid RGB colors.


def main():
    # Set all of the colours to 0
    red = 0
    green = 0
    blue = 0
    # Print what the program does
    print("I am going to display all RGB numbers.")
    # For loop to go through all red numbers
    for red in range(256):
        # For loop to go through all green numbers
        for green in range(256):
            # For loop to go through all blue numbers
            for blue in range(256):
                # print("RGB = ({0}, {1}, {2})". format(red, green, blue))
                # - Print each colour in the colour it represents
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        red,
                        green,
                        blue,
                        "RGB(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                    )
                )
                # (red, green, blue, “RGB(“ + r + “,” + g + “,” + b + “)”))


if __name__ == "__main__":
    main()
