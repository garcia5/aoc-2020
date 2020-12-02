input_dict = {int(k): 1 for k in open('input1', 'r').read().splitlines()}

for year1 in input_dict.keys():
    for year2 in input_dict.keys():

        if year1 + year2 > 2020:
            continue

        if (2020 - year1 - year2) in input_dict.keys():
            print(f'{year1} {year2} {2020-year1-year2}')
            print(year1 * year2 * (2020-year1-year2))
            exit()
