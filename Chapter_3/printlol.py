"""the following function take one argument, a list, and
prints each element of the list"""


def print_lol(lst): #1st examle of recursion in python
    """This recursive for loop makes a call to the present function if the list contains a list of lists
    . When print_lol is called again if that nested list is not does not contain a list of lists each item 
    in that list is printed then the other higher list elements are printed."""
    for each item in lst:
        if instanceof(item, lst):
            print_lol(item)
        else:
            print(item)
        