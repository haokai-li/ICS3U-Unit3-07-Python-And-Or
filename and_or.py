#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program is about 'and' and 'or'


def main():
    # This function is about 'and' and 'or'

    # input
    user_string = input("Please enter your age: ")
    print("")

    # process
    try:
        user_number = int(user_string)
        if user_number >= 25 and user_number <= 40:
            # output
            print("You are accepted to date my grandchild.")
        elif user_number < 25:
            # output
            print("You are too young!.")
        else:
            # output
            print("You are too old!.")
    except Exception:
        # output
        print("{} is not a valid input.".format(user_string))

    print("\nDone.")


if __name__ == "__main__":
    main()
