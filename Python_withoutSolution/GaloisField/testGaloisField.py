# -*- coding: utf-8 -*-
# Name of file: test.py
# import numpy package
import numpy as np

# import F_256 Galois Field module
import my_gf_functions as gf


################################################################################
#
#  Define the Logtable and and its inverse Alogtable for all elements in F_256
#  as global variables
#
#  outputs: let g^i is in integer form, where g is a generator of F_256
#  - Logtable[g^i]=i for i=0,..,254 by convention Logtable[0]=0
#  - Alogtable[i]=g^i for i=0,..,255
#
################################################################################
def Generate_Logtable_Alogtable():
    # define the generator of F_256
    g = int("0x03", 16)
    # initialize Logtable
    Logtable = np.zeros(256, dtype="int")
    Alogtable = np.zeros(256, dtype="int")

    index = g

    for i in range(254):
        index = gf.mul_xtime(index, g)
        Logtable[index % 256] = i + 2
        Alogtable[i + 2] = index % 256

    Alogtable[0] = 1
    Alogtable[1] = g
    Logtable[1] = 0

    Logtable[3] = 1

    return Logtable, Alogtable


################################################################################
# Tabular representation of xtime(xy)
################################################################################
"""FILL IN MISSING CODE"""


def Question1_1():
    # we use custom arrays to avoid numpy type system
    array = []
    for x in range(16):
        line = []
        for y in range(16):
            hex_x = hex(x)[2:]
            hex_y = hex(y)[2:]

            xy = f"0x{hex_x}{hex_y}"  # concatenation of hex values

            b = bin(int(xy, base=16))[2:]

            res = gf.xtime(int(b, 2))
            line.append({xy: hex(res)})
        array.append(line)

    for k in array:
        print(k)


Question1_1()
################################################################################
# Example of addition in F_256
################################################################################
# a1='0xa1' in hexadecimal form converted to integer form
a1 = int("0xa1", 16)
# b1='0x12' in hexadecimal form converted to integer form
b1 = int("0x12", 16)
# print a1+b1='0xb3' in hex form
"""FILL IN MISSING CODE"""


def Question1_2():
    res = gf.add(a1, b1)
    res = hex(res)
    print(res)


Question1_2()

################################################################################
# Example of slow multiplication in F_256 using xtime()
################################################################################
# a2='0x57' in hexadecimal form converted to integer form
a2 = int("0x57", 16)
# b2='0x83' in hexadecimal form converted to integer form
b2 = int("0x83", 16)
# print a2*b2='0xc1' in hex form
"""FILL IN MISSING CODE"""


def Question1_3():
    res = gf.mul_xtime(a2, b2)
    print(hex(res))


Question1_3()

################################################################################
# Show that a='0x03' generates F_256
################################################################################

print("powers of the generator:\n")


# print all powers of a
def Question1_4():
    a = int("0x03", 16)
    b = a
    F256 = set()
    for i in range(256):
        if i == 0:
            tmp = int("0x01", 16)
            F256.add(tmp)
        else:
            b = gf.mul_xtime(b, a)
            F256.add((b))
        print("a^", i, "=", hex(b), "\n")

    print((F256))  # contains all integers from 1 to 255


Question1_4()

################################################################################
# Galois Field F_256 parameters using irreducible polynomial m(x)=x^8+x^4x^3+x+1
################################################################################
# generate Logtable and Alogtable
[Logtable, Alogtable] = Generate_Logtable_Alogtable()
# print Logtable
for i in range(256):
    print("Logtable[", i, "]=", Logtable[i])
    if i % 16 == 15:
        print("\n")
# print Alogtable
for i in range(256):
    print("Alogtable[", i, "]=", Alogtable[i])
    if i % 16 == 15:
        print("\n")

################################################################################
# Example of fast multiplication in F_256 using Logtable() and Alogtable()
################################################################################
# a2='0x57' in hexadecimal form converted to integer form
a2 = int("0x57", 16)
# b2='0x83' in hexadecimal form converted to integer form
b2 = int("0x83", 16)
# print a2*b2='0xc1' in hex form

print("a2*b2", gf.mul(a2, b2))

################################################################################
# Example of fast inversion in F_256 using Logtable() and Alogtable()
################################################################################
# a='0x83' in hexadecimal form converted to integer form
a = int("0x83", 16)
a_inv = gf.inv(a)

# print a^{-1}='0x80'
print("a^{-1}=", hex(a_inv))

################################################################################
# Example of fast division in F_256 using Logtable() and Alogtable()
################################################################################
# a='0x01' in hexadecimal form converted to integer form
a = int("0x01", 16)
# a='0x83' in hexadecimal form converted to integer form
b = int("0x83", 16)
res = gf.div(a, b)
# print a/b='0x80'
print("a/b=", hex(res))


print("0B * 2 = ", gf.mul(int("0x1B", 16), 2))
