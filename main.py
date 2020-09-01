def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y


if __name__ == '__main__':
    print("Hello, I'm calculator!")
