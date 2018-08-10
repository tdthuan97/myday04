def right_triangle_errors(a, b, c):
    arr = [a, b, c]
    right = []
    try:
        right = [s for s in arr if int(s) > 0]
        right.sort()
        if len(right) == 3:
            return right[0] ** 2 + right[1] ** 2 == right[2] ** 2
        raise ValueError('Incorrect value')
    except ValueError:
        raise ValueError('Incorrect value')
