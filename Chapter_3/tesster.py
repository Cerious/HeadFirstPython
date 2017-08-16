
def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    return arr


def zero_out(lyst):
    del lyst[:]
    return lyst

def neighbors(args):
    lyst_one = args[:]
    lyst_two = args[:]
    neighbor = []
    if args.index(0) == 0:
        swap_1 = swap(lyst_one, 0, 1) #save the swap to a variable
        swap_2 = swap(lyst_two, 0, 3) # save the 2nd potential swap to a variable
        neighbor = [lyst_one, lyst_two]
    return neighbor

lyst_1 = [0,2,5,3,4,1,6,7,8]
print(f"Neighbors Final: {neighbors(lyst_1)}")
