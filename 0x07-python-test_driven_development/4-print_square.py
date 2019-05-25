def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) < 0:
        raise TypeError('size must be an integer')

    for i in range(0, size):
        for j in range(1, (size + 1)):
            print('#', end="")
        print()
