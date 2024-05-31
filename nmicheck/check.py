import math


def nmi_checksum(nmi: str) -> int:
    """Return the checksum digit of an NMI"""
    if len(nmi) != 10:
        msg = "NMI must be 10 digits"
        raise ValueError(msg)
    total = 0
    for i, char in enumerate(reversed(nmi)):
        val_ascii = ord(char)
        val = val_ascii if i % 2 == 1 else val_ascii * 2
        to_add = sum(map(int, str(val)))
        total += to_add

    next_ten = math.ceil(total / 10.0) * 10
    checksum = next_ten - total
    return checksum


def checksum_valid(nmi: str) -> bool:
    """Return whether the 11th checksum digit is valid"""
    if len(nmi) != 11:
        msg = "NMI must be 11 digits"
        raise ValueError(msg)
    start = nmi[0:10]
    try:
        checksum = int(nmi[10])
    except ValueError:
        return False  # Checksum must be an integer
    if checksum == nmi_checksum(start):
        return True
    return False
