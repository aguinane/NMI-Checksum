import pytest

from nmicheck import nmi_participant

EXAMPLE_NMIS = [
    ("NGGG000000", "ACTEWP"),
    ("2001985733", "UMPLP"),
    ("7102000001", None),
    ("QAAAVZZZZZ", "ERGONETP"),
    ("QCDWW00010", "PLINKP"),
    ("VAAA000000", "CITIPP"),
    ("VKTS876510", None),
]


@pytest.mark.parametrize("nmi,participant", EXAMPLE_NMIS)
def test_participant_lookup(nmi, participant):
    """Test the participant lookup"""
    assert nmi_participant(nmi) == participant
