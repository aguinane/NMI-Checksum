import math
import warnings


def nmi_checksum(nmi: str) -> int:
    """Return the checksum digit of an NMI"""
    if len(nmi) != 10:
        msg = "NMI must be 10 digits to generate checksum"
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


def nmi_checksum_valid(nmi: str) -> bool:
    """Return whether the 11th checksum digit is valid"""
    if len(nmi) != 11:
        msg = "NMI must be 11 digits to validate checksum"
        raise ValueError(msg)
    start = nmi[0:10]
    try:
        checksum = int(nmi[10])
    except ValueError:
        return False  # Checksum must be an integer
    return checksum == nmi_checksum(start)


def checksum_valid(nmi: str) -> bool:
    """Deprecated function call for nmi_checksum_valid"""
    msg = "The checksum_valid function should be changed to nmi_checksum_valid."
    warnings.warn(msg, DeprecationWarning, stacklevel=2)
    return nmi_checksum_valid(nmi)


def nmi_valid(nmi: str) -> bool:
    """Return whether a NMI is valid"""
    # Full NMIs for validation must be 11 characters (11th digit is checksum)
    if len(nmi) != 11:
        return False
    # Character letters ‘O’ and ‘I’ are not permitted
    # in order to avoid confusion with numbers 0 and 1.
    if "O" in nmi:
        return False
    if "I" in nmi:
        return False
    # Finally check whether the checksum is valid
    return nmi_checksum_valid(nmi)
