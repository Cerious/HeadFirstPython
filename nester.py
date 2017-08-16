    q def print_lol(the_list, indent = False,level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, True, level+1)
        else:
            if indent == True:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)

lyst = [1,2,3,[4,5],6]
print_lol(lyst,True, 0)    