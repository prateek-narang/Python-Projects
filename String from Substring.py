# check if a given string can be fully constructed from any of its substring

s = 'abcabcabcabc'


# s = 'abababab'

def getSubstringsLengths(s):
    '''get lengths of all possible substrings that can make the full string'''
    _len = len(s)
    _arr = []
    for x in range(1, _len + 1):
        if (x != _len) and (_len % x == 0):
            _arr.append(x)
    return _arr


def checkSubstring(len_s, s):
    '''check whether any substring length is making the full string'''
    flag = 0
    for x in len_s:
        _temp = ''
        for y in range(0, len(s), x):
            ele = s[y:y + x]

            if y == 0:
                _temp = ele
            elif _temp != ele:
                break

            if y == (len(s) - x):
                flag = 1

    return flag


if len(s) == 1:
    print(0)
else:
    len_s = getSubstringsLengths(s)
    print(checkSubstring(len_s, s))