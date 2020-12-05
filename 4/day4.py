import re

REQUIRED = {
    "byr": (lambda p: int(p) >= 1920 and int(p) <= 2002),
    "iyr": (lambda p: re.search(re.compile(r"20[1-2]\d"), p)),
    "eyr": (lambda p: re.search(re.compile(r"20[2-3]\d"), p)),
    "hgt": (
        lambda p: int(p[:-2]) >= 150 and int(p[:-2]) <= 193 if p.endswith("cm")
        else p.endswith("in") and int(p[:-2]) >= 59 and int(p[:-2]) <= 76
    ),
    "hcl": (lambda p: re.search(re.compile(r"#[0-9a-f]{6}"), p.lower())),
    "ecl": (lambda p: p.lower() in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": (lambda p: re.search(re.compile(r"^\d{9}$"), p)),
}


def valid(passport):
    for f, r in REQUIRED.items():
        if f not in passport.keys():
            return False

        if not r(passport[f]):
            return False

    return True


if __name__ == "__main__":
    count = 0
    passport = {}

    for l in open("input", "r").read().splitlines():
        l.strip()

        if len(l) == 0:
            if valid(passport):
                count = count + 1
            passport = {}

        for w in l.split():
            w = w.split(":")
            passport[w[0]] = w[1]

    if valid(passport):
        count = count + 1

    print(count)
