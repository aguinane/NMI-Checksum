import hashlib

from .check import nmi_checksum


def short_nmi(nmi: str) -> str:
    """Truncate a NMI to 10 characters"""
    return nmi[:10].upper()


def long_nmi(nmi: str) -> str:
    """Expand a NMI to 11 characters"""
    short = short_nmi(nmi)
    return short + str(nmi_checksum(short))


def obfuscate_nmi(nmi: str, salt: str = "secret", length: int = 20) -> str:
    """Make a pseudo anonymous version of the NMI"""
    clean = short_nmi(nmi)
    salted = f"{salt}-{clean}"
    nmi_hash = hashlib.sha256(salted.encode("utf-8")).hexdigest().upper()
    return nmi_hash[:length]
