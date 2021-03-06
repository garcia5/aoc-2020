import re


class Policy:
    def __init__(self, _policy_str):
        match_dict = re.match(r'(?P<low>^\d+)-(?P<high>\d+) (?P<char>\w):',
                              _policy_str).groupdict()
        self.first = int(match_dict['low']) - 1
        self.second = int(match_dict['high']) - 1
        self.char = match_dict['char']


class Password:
    def __init__(self, _policy_str):
        match_dict = re.match(r'^.*:(?P<passwd>.*)$', _policy_str).groupdict()
        self.password = match_dict['passwd'].strip()

    def is_valid(self, policy):
        return (self.password[policy.first]
                == policy.char) != (self.password[policy.second]
                                    == policy.char)


if __name__ == '__main__':
    count = sum([
        1 for l in open('input', 'r').read().splitlines()
        if Password(l).is_valid(Policy(l))
    ])

    print(count)
