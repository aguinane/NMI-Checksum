# NMI-Checksum

A library to validate National Metering Identifiers (NMIs)

The validation rules are as per the Australian [National Metering Identifier Procedure](https://aemo.com.au/Electricity/National-Electricity-Market-NEM/Retail-and-metering/-/media/EBA9363B984841079712B3AAD374A859.ashx).

## Usage

```python
from nmicheck import nmi_checksum
checksum = nmi_checksum("QAAAVZZZZZ")
print(checksum)  # 3
```

```python
from nmicheck import nmi_checksum_valid
print(nmi_checksum_valid("QAAAVZZZZZ3"))  # True
print(nmi_checksum_valid("QAAAVZZZZZ0"))  # False
```

```python
from nmicheck import long_nmi, short_nmi
print(long_nmi("NMI00012345"))  # NMI000123458
print(short_nmi("NMI000123458"))  # NMI00012345
```

```python
from nmicheck import obfuscate_nmi
print(obfuscate_nmi("NMI00012345", salt="secret"))  # 0E6816DCBA334A7B2DEF
print(obfuscate_nmi("NMI00012345", salt="secret", length=10))  # 0E6816DCBA
```

You can also look up the participant code for a particular NMI (which DNSP or TNSP) based on the [NMI Allocation List](https://www.aemo.com.au/-/media/Files/Electricity/NEM/Retail_and_Metering/Metering-Procedures/NMI-Allocation-List.pdf).

```python
from nmicheck import nmi_participant

participant = nmi_participant("6102000000")
print(participant)  # CITIPP

participant = nmi_participant("3202000000")
print(participant)  # PLINKP
```