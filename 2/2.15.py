# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

def test2():
    # Write test cases that achieve 100% 
    # Statement coverage of add8. You 
    # will need to call add8 multiple 
    # times in order to do this.
    ###Your code here.
    for a in range(0, 256):
        for b in range(0, 256):
            for c in [False, True]:
                assert call_add8(a, b, c) == a + b + (1 if c else 0)


    pass
def test():
    assert call_add8(0, 0, 0) == 0
    assert call_add8(255, 255, 1) == 511

def call_add8(a, b, c):
    a = int2bits(a)
    b = int2bits(b)
    bits = add8(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7],
         b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7],
         c)
    return bits2int(bits)

def bits2int(bits):
    bits = list(reversed(bits))
    str = ''.join([ ('1' if bit else '0') for bit in bits ])
    return int(str, 2)

def int2bits(i):
    return list(reversed([ (True if bit=='1' else False) for bit in bin(i)[2:].zfill(8) ]))

def test_helpers():
    assert bits2int(int2bits(1)) == 1
    assert bits2int(int2bits(15)) == 15
    assert bits2int(int2bits(154)) == 154

test_helpers()

test()