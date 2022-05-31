#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program converts a level to it's correlating percentage.


def conversion(level):
    # this function converts a level to percentage

    # process
    if level == "4+":
        percentage = 97

    elif level == "4":
        percentage = 91

    elif level == "4-":
        percentage = 83

    elif level == "3+":
        percentage = 78

    elif level == "3":
        percentage = 75

    elif level == "3-":
        percentage = 71

    elif level == "2+":
        percentage = 68

    elif level == "2":
        percentage = 65

    elif level == "2-":
        percentage = 61

    elif level == "1+":
        percentage = 58

    elif level == "1":
        percentage = 55

    elif level == "1-":
        percentage = 51

    elif level == "R":
        percentage = 30

    else:
        percentage = -1

    return percentage


def main():
    # this function gets input, calls a function, gives output

    # input
    level = input("Enter a level to see it’s correlating percentage: ")

    percentage = conversion(level)

    if percentage == -1:
        print("\nThat level is invalid. Please Re-Run.")
    else:
        print("\nLevel {0} correlates to {1}%.".format(level, percentage))

    print("\nDone.")


if __name__ == "__main__":
    main()
