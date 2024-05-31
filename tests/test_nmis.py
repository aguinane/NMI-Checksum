import pytest

from nmicheck import checksum_valid, nmi_checksum

EXAMPLE_CHECKSUMS = [
    ("2001985732", 8),
    ("2001985733", 6),
    ("7102000001", 7),
    ("QAAAVZZZZZ", 3),
    ("QCDWW00010", 2),
    ("VKTS876510", 8),
]


@pytest.mark.parametrize("nmi,checksum", EXAMPLE_CHECKSUMS)
def test_checksum(nmi, checksum):
    """Test the checksum calculation"""
    assert nmi_checksum(nmi) == checksum


@pytest.mark.parametrize("nmi,checksum", EXAMPLE_CHECKSUMS)
def test_validate(nmi, checksum):
    """Test the checksum calculation"""

    full_nmi = f"{nmi}{checksum}"
    assert checksum_valid(full_nmi)


def test_bad_checksum():
    """Test the checksum fails"""

    full_nmi = "QAAAVZZZZZX"
    assert not checksum_valid(full_nmi)
