import hashlib

key = "yzbqklnj"

def part1():
    i = 0
    h = ""
    while not h.startswith("00000"):
        i += 1
        str_to_hash = key + str(i)
        bytes_to_hash = bytes(str_to_hash, "ascii")
        h = hashlib.md5(bytes_to_hash).hexdigest()

    print("Number resulting in 5 leading zeros: {}".format(i))

def part2():
    # The first number to start with 5 zeros is 282749, so 6 zeros can't come before that.
    i = 282749
    h = ""
    while not h.startswith("000000"):
        i += 1
        str_to_hash = key + str(i)
        bytes_to_hash = bytes(str_to_hash, "ascii")
        h = hashlib.md5(bytes_to_hash).hexdigest()

    print("Number resulting in 6 leading zeros: {}".format(i))

part1()
part2()
