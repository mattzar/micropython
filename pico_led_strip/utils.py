
def read_file(filename, mode='r'):
    file = open(filename, mode)
    return tuple(line.rstrip('\n\r').split(',') for line in file)

def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i

def is_iterable(element):
    try:
        iter(element)
    except TypeError:
        return 0
    else:
        return 1


def main():
    print(is_iterable([1,2,3]))

if __name__ == "__main__":
    main()