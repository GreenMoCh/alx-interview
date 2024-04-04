#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determins if a given data set represents a valid UTF-8 encoding
    """
    n_bytes = 0

    for num in data:
        bin_representation = format(num, '#010b')[-8:]

        if n_bytes == 0:
            for bit in bin_representation:
                if bit == '0': break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        
        else:
            if not (bin_representation[0] == '1' and bin_representation[1] == '0'):
                return False

        n_bytes -= 1

        if n_bytes > 0:
            continue

        if n_bytes == 0:
            n_bytes = 0

    return n_bytes == 0
    