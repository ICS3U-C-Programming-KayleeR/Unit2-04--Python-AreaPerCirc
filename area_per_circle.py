#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 30,09,2026
# The program calculates the area and
# perimeter of
# a circle by asking the user to
# input the radius. The program then displays
# the output.

import math


def main():
    # user input, ask user for radius
    radius = float(input("Enter the radius of the circle (cm): "))

    # calculation process using Pi
    area = math.pi * (radius**2)
    circumference = math.pi * (radius * 2)

    # display the area and circumference
    print("The area of the circle is = {:.2f}".format(area))
    print("The circumference of the circle is = {:.2f}".format(circumference))


if __name__ == "__main__":
    main()
