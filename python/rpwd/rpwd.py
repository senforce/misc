#!/usr/bin/env python

import math
import random
import string
import sys


def gen_random_str(length, ratio=[1,1,1]):
    ratio_digit = ratio[0] * 26
    ratio_lower = ratio[1] * 10
    ratio_upper = ratio[2] * 10
    gcd = math.gcd(ratio_digit, math.gcd(ratio_lower, ratio_upper))
    ratio_digit //= gcd
    ratio_lower //= gcd
    ratio_upper //= gcd
    print('gen_random_str.ratio = ', len(string.digits) * ratio_digit, len(string.ascii_lowercase) * ratio_lower, len(string.ascii_uppercase) * ratio_upper)
    src_str = string.digits * ratio_digit + string.ascii_lowercase * ratio_lower + string.ascii_uppercase * ratio_upper
    return ''.join([random.choice(src_str) for i in range(length)])



def main():
    argc = len(sys.argv)
    if argc < 2:
        print('[CMD] length')
        exit(-1)
    length = int(sys.argv[1])

    ratio = [2, 3, 3]

    print(ratio)
    rand_str = gen_random_str(length, ratio)
    print()
    print(rand_str)


if __name__ == '__main__':
    main()

