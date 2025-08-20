PARTICIPANT_PREFIXES = {
    "2001": "UMPLP",
    "2102": "ETSATP",
    "2500": "PWCLNSP",
    "2503": "PWCLNSP",
    "30": "ERGONETP",
    "31": "ENERGEXP",
    "3202": "PLINKP",
    "4001": "CNRGYP",
    "4102": "ENERGYAP",
    "4204": "CNRGYP",
    "4310": "INTEGP",
    "4407": "CNRGYP",
    "4508": "CNRGYP",
    "4608": "TRANSGP",
    "6001": "SOLARISP",
    "6102": "CITIPP",
    "6203": "POWCP",
    "6305": "EASTERN",
    "6407": "UNITED",
    "6509": "GPUPP",
    "7001": "ACTEWP",
    "8000": "AURORAP",
    "8590": "AURORAP",
    "NAAA": "CNRGYP",
    "NBBB": "CNRGYP",
    "NCCC": "ENERGYAP",
    "NDDD": "CNRGYP",
    "NEEE": "INTEGP",
    "NFFF": "CNRGYP",
    "NGGG": "ACTEWP",
    "NTTT": "TRANSGP",
    "QAAA": "ERGONETP",
    "QB": "ENERGEXP",
    "QCCC": "ERGONETP",
    "QDDD": "ERGONETP",
    "QEEE": "ERGONETP",
    "QFFF": "ERGONETP",
    "QGGG": "ERGONETP",
    "SAAA": "UMPLP",
    "SASMPL": "UMPLP",
    "T00000": "AURORAP",
    "VAAA": "CITIPP",
    "VBBB": "EASTERN",
    "VCCC": "POWCP",
    "VDDD": "SOLARISP",
    "VEEE": "UNITED",
}

TNI_PREFIXES = {
    "Q": "PLINKP",
    "A": "ACTEWP",
    "S": "ETSATP",
    "T": "TRANSEND",
    "V": "GPUPP",
}


def nmi_participant(nmi: str) -> str | None:
    """Attempt to determine the partipant associated with the NMI"""
    nmi = nmi.upper().strip()  # Normalize input

    # Check if W is 5th character and associate to TNSP
    if nmi[4] == "W":
        for prefix in TNI_PREFIXES:
            if nmi.startswith(prefix):
                return TNI_PREFIXES[prefix]

    # Check for DNSP
    for prefix in PARTICIPANT_PREFIXES:
        if nmi.startswith(prefix):
            return PARTICIPANT_PREFIXES[prefix]

    # Could not match
    return None
