def shunxu(li, var):
    for index, v in enumerate(li):
        if v == var:
            return index
    else:
        return None

if __name__ == '__main__':
    lis = [1, 3, 4, 5, 67, 8]
    print(shunxu(lis, 67))