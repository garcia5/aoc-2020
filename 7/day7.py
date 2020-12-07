import re

rules = {}
DONE = 'no other bags'

def line_to_rule(line):
    match_dict = re.match(r'(?P<key>^.*) bags contain (?P<vals_to_parse>.*).',
            line).groupdict()

    key = match_dict['key'].strip()
    vals = match_dict['vals_to_parse'].strip()
    if vals == DONE:
        rules[key] = vals

    else:
        rules[key] = {}
        # read in bags that `key` contains
        for b in vals.split(', '):
            match_dict = re.match(r'(?P<count>^\d) (?P<bag>.*) bag.*$', b)
            rules[key][match_dict['bag']] = int(match_dict['count'])

def color_in_path(key, color='shiny gold'):
    if rules[key] == DONE:
        return False

    if color in rules[key].keys():
        return True

    for r in rules[key].keys():
        if color_in_path(r, color):
            return True

def bag_count(key='shiny gold'):
    if rules[key] == DONE:
        return 0

    this_bag_contains = 0
    for color, count in rules[key].items():
        this_bag_contains += (count * bag_count(color)) + count

    return this_bag_contains


for l in open('input', 'r'):
    line_to_rule(l.strip())

# count = 0
# for r in rules.keys():
    # if color_in_path(r):
        # count += 1

print(bag_count())
