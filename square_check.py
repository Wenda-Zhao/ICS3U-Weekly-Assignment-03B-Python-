#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Nov 2020
# This program is for square check


def main():
    # this function is for square check

    # input
    length = int(input("Enter the Length: "))
    width = int(input("Enter the width: "))

    # process
    if length == width and length > 0 and width > 0:
        # output
        print("It is a square.")
    # process
    else:
        # output
        print("It is not a square.")


if __name__ == "__main__":
    main()
