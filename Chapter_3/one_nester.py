"""the following function take one argument, a list, and
prints each element of the list"""
import sys

def print_lol(lyst, indent=False, level=0, location=sys.stdout ): #1st examle of recursion in python
    """This recursive for loop makes a call to the present function if the list contains a list of lists
    . When print_lol is called again if that nested list is not does not contain a list of lists each item
    in that list is printed then the other higher list elements are printed."""
    for each_item in lyst:
        if isinstance(each_item, lyst):
            print_lol(each_item, indent, level + 1, location)

        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=location)
                print(each_item, file=location)
