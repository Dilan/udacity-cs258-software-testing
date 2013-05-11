# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
#
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies
# whether it is valid or not. If it is valid, it returns True,
# otherwise it returns False.


def is_luhn_valid(n):
    ###Your code here.

    n = str(n)
    digits = [int(x) for x in list(n)]

    double_offset = 0 if len(digits) % 2 == 0 else 1
    normal_offset = 1 if len(digits) % 2 == 0 else 0

    double_digits = digits[double_offset::2]
    normal_digits = digits[normal_offset::2]

    double_sum = sum([2*x-9 if 2*x > 9 else 2 * x for x in double_digits])
    normal_sum = sum([x for x in normal_digits])

    total = normal_sum + double_sum

    return total % 10 == 0


def test():
    assert(is_luhn_valid('5108050116082780')) is True
    assert(is_luhn_valid('4242424242424242')) is True
    assert(is_luhn_valid('4111111111111111')) is True
    assert(is_luhn_valid('4235190001963642')) is True
    assert(is_luhn_valid('5105105105105100')) is True
    assert(is_luhn_valid('5555555555554444')) is True
    assert(is_luhn_valid('5431111111111111')) is True
    assert(is_luhn_valid('6011601160116611')) is True
    assert(is_luhn_valid('1234'))             is False
    assert(is_luhn_valid('1234123412341234')) is False
    assert(is_luhn_valid('5105105105105100')) is True
    assert(is_luhn_valid('378282246310005'))  is True
    assert(is_luhn_valid('6011601160116611')) is True
    assert(is_luhn_valid('371449635398431'))  is True
    assert(is_luhn_valid('378282246310005'))  is True


test()
