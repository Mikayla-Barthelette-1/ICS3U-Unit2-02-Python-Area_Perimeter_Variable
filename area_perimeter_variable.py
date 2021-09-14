#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program finds the area and perimeter of a rectangle


def main():
    # this function calculates the area and perimeter

    # input
    length = int(
        input("Enter the length of the rectangle as an integer (mm): ")
    )
    width = int(input("Enter the width of the rectangle as an integer (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print(" ")
    print("The area is {0} mm².".format(area))
    print("The perimeter is {0} mm.".format(perimeter))
    print(" ")
    print("Done.")


if __name__ == "__main__":
    main()
