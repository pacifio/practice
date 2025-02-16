CHECK_NUMBER = "17893729974"

"""
def eff_luhn():
    n = int(CHECK_NUMBER[-1])
    total = 0
    for i, d in enumerate(reversed(CHECK_NUMBER[:-1])):
        # x = int(d)*(2-i % 2)
        # total += x//10+x % 10
        x = int(d)*(1+i % 2)
        total += x // 10 + x
    # return (10-(total%10))%10 == int(n)
    # return n-10 == -(total%10)
    # return -10 == -(total%10) - n
    # return 0 == -(total%10) - n + 10
    # return 0 == -(n-10+total % 10)
    return total % 10 == 0
"""
LOOKUP = dict(zip('0123456789', (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)))
LOOKUPS = (
    dict(zip('0123456789', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))),
    dict(zip('0123456789', (0, 2, 4, 6, 8, 1, 3, 5, 7, 9))),
)


def luhn(digits: str) -> int:
    digits = digits[:-1]
    reversed_check_number = digits[::-1]
    last_num = reversed_check_number[-1]
    non_multiply = []
    multiplied = []
    sums = []
    [non_multiply.append(int(reversed_check_number[i]))
     for i in range(1, len(reversed_check_number)-1, 2)]
    [multiplied.append(list(str(int(reversed_check_number[i])*2))[::-1])
     for i in range(0, len(reversed_check_number), 2)]
    [sums.append(int(i[0]) + int(i[1])) for i in multiplied]
    sum_digits = sum(non_multiply) + sum(sums) + int(last_num)
    return (10-(sum_digits % 10)) % 10


def verify_imperative(digits: str) -> bool:
    n = int(digits)
    total = 0
    for i, d in enumerate(reversed(digits)):
        x = int(d)*(1+i % 2)
        total += x // 10 + x
    return total % 10 == 0


def f(args):
    i, d = args
    x = int(d)*(1+(i % 2))
    return x // 10 + x


def verify_functional(digits: str) -> bool:
    return sum(map(f, enumerate(reversed(digits)))) % 10 == 0


def verify_functional_smaller(digits: str) -> bool: return sum(map(lambda x: (int(
    x[1])*(1+x[0] % 2))//10+int(x[1])*(1+x[0] % 2), enumerate(reversed(digits)))) % 10 == 0


def verify_functional_lookup(digits: str) -> bool:
    total = 0
    for i, d in enumerate(reversed(digits[:-1])):
        if i % 2 == 0:
            total += LOOKUP[d]
        else:
            total += int(d)
    total += int(digits[-1])
    return total % 10 == 0


def verify_functional_lookup_2(digits: str) -> bool:
    return (sum([LOOKUP[d] if i % 2 == 0 else int(d)
                for i, d in enumerate(reversed(digits[:-1]))]) + int(digits[-1])) % 10 == 0


def verify_functional_lookup_optimized(digits: str) -> bool:
    return sum(LOOKUPS[i % 2][d] for i, d in enumerate(reversed(digits))) % 10 == 0


if __name__ == "__main__":
    functions = [luhn, verify_imperative,
                 verify_functional_smaller, verify_functional_lookup, verify_functional_lookup_2, verify_functional_lookup_optimized]
    for f in functions:
        print(f(CHECK_NUMBER))
    print("ok")
