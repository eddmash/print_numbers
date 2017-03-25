
def get_range_func():
    """
    Gets the right range function to use base on python version in use.

    The function returned will return a generator object instead of the actaul list,
    this way we save on memory incase when we need to generate very many items.

    On py2 xrange returns a generator object whilst range returns the actual list
    On py3 range returns a generator object
    """
    try:
        xrange
    except NameError:
        xrange = range
    return xrange


def is_multiple(n, x):
    """Check if n is multiple of x"""
    return n % x == 0


def do_print(start, end):
    """
    Output number from start to end.

    But for multiples of three print "Three" instead of the number and
    for the multiples of five print "Five".
    For numbers which are multiples of both three and five print "ThreeFive".
    
    """
    ranger = get_range_func()
    for n in ranger(start, end):
        if is_multiple(n, 5) and is_multiple(n, 3):
            print("ThreeFive")
        elif is_multiple(n, 3):
            print("Three")
        elif is_multiple(n, 5):
            print("Five")
        else:
            print(n)


if __name__ == "__main__":
    do_print(1, 100)
