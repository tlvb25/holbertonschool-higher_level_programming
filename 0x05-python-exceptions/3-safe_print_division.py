#!/usr/bin/python3
def safe_print_quotientision(a, b):
    try:
        quotient = a / b
    except ZeroquotientisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
    