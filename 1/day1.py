input = open('input1', 'r').read().splitlines()

for i, lni in enumerate(input):
    for j, lnj in enumerate(input):
        for k, lnk in enumerate(input):
            lni = int(lni)
            lnj = int(lnj)
            lnk = int(lnk)
            if lni + lnj + lnk == 2020:
                res = lni * lnj * lnk
                print(f'y1: {lni}, y2: {lnj}, y3: {lnk}, y1 * y2 * y3 = {res}')
                exit()
