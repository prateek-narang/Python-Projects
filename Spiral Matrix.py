# Print NxN Matrix elements in Spiral fashion

def isOutbound(i, j):
    if i < 0 or i >= _len or j < 0 or j >= _len:
        return True
    else:
        return False


def spiralMatrix(arr):
    res = []
    i = 0
    j = 0
    _elem = _len ** 2
    _add = []
    _dir = 1

    for a in range(_elem):
        res.append(arr[i][j])
        _add.append((i, j))

        if _dir == 1:
            if (i, j + 1) in _add or isOutbound(i, j + 1):
                _dir += 1
                i += 1
            else:
                j += 1
        elif _dir == 2:
            if (i + 1, j) in _add or isOutbound(i + 1, j):
                _dir += 1
                j -= 1
            else:
                i += 1
        elif _dir == 3:
            if (i, j - 1) in _add or isOutbound(i, j - 1):
                _dir += 1
                i -= 1
            else:
                j -= 1
        elif _dir == 4:
            if (i - 1, j) in _add or isOutbound(i - 1, j):
                _dir = 1
                j += 1
            else:
                i -= 1
    return res


_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
_len = len(_input)
print(spiralMatrix(_input))