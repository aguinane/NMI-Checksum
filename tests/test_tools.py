import pytest

from nmicheck.tools import long_nmi, obfuscate_nmi

EXAMPLE_CHECKSUMS = [
    ("2001985732", 8),
    ("2001985733", 6),
    ("7102000001", 7),
    ("QAAAVZZZZZ", 3),
    ("QCDWW00010", 2),
    ("qcdww00010", 2),
    ("VKTS876510", 8),
]


EXAMPLE_HASHES = [
    ("2001985732", "6D34CC122D491FC199BC"),
    ("20019857328", "6D34CC122D491FC199BC"),
    ("QCDWW00010", "2B6672795F589E3AA0D2"),
    ("qcdww00010", "2B6672795F589E3AA0D2"),
    ("VKTS876510", "4BB52AD1D75AF68F0B91"),
]


@pytest.mark.parametrize("nmi,checksum", EXAMPLE_CHECKSUMS)
def test_long_nmi(nmi, checksum):
    """Test the checksum expansion of NMIs"""

    assert long_nmi(nmi) == f"{nmi}{checksum}".upper()


@pytest.mark.parametrize("nmi,hashed", EXAMPLE_HASHES)
def test_obfuscated_nmi(nmi, hashed):
    """Test the obfuscattion of NMIs"""
    assert obfuscate_nmi(nmi) == hashed
    assert obfuscate_nmi(nmi, salt="newsecret") != hashed
