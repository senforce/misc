#!/usr/bin/env python

import math
import random
import string
import sys


def gen_random_str(length, ratio=[1,1,1]):
    ratio_digit = ratio[0] * len(string.digits)
    ratio_lower = ratio[1] * len(string.ascii_lowercase)
    ratio_upper = ratio[2] * len(string.ascii_uppercase)
    gcd = math.gcd(ratio_digit, ratio_lower, ratio_upper)
    ratio_digit //= gcd
    ratio_lower //= gcd
    ratio_upper //= gcd
    print('gen_random_str.ratio = ', ratio_digit, ratio_lower, ratio_upper)
    lcm = math.lcm(ratio_digit, ratio_lower, ratio_upper)
    mul_digit = lcm // ratio_digit
    mul_lower = lcm // ratio_lower
    mul_upper = lcm // ratio_upper
    print('gen_random_str.mul = ', mul_digit, mul_lower, mul_upper)
    src_str = string.digits * mul_digit + string.ascii_lowercase * mul_lower + string.ascii_uppercase * mul_upper
    return ''.join([random.choice(src_str) for i in range(length)])



def main():
    argc = len(sys.argv)
    if argc < 2:
        print('[CMD] length')
        exit(-1)
    length = int(sys.argv[1])
    rand_str = gen_random_str(length, [3, 4, 4])
    print(rand_str)


if __name__ == '__main__':
    main()

