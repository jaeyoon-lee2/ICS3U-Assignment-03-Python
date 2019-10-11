#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program display which number is bigger


import random


def main():
    # this function display which number is bigger

    # input
    integer1_as_string = input("Enter the first number (integer): ")
    integer2_as_string = input("Enter the second number (integer): ")

    # process & output
    try:
        integer1_as_number = int(integer1_as_string)
        integer2_as_number = int(integer2_as_string)
        if integer1_as_number > integer2_as_number:
            print("The first number ({0}) is bigger than the second " +
                  "number ({1})."
                  .format(integer1_as_number, integer2_as_number))
        elif integer1_as_number < integer2_as_number:
            print("The second number ({1}) is bigger than the first " +
                  "number ({0})."
                  .format(integer1_as_number, integer2_as_number))
        else:
            print("Those numbers are the same.")
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
