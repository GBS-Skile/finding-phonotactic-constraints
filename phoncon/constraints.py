import re
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class NaturalClass:
    entries: List[Tuple[str, str]]  # (<feature name>, <value>)
    complement: bool = False

    def __str__(self) -> str:
        result = "["
        if self.complement:
            result += "^"
        result += ",".join(v + k for k, v in self.entries)
        return result + "]"


@dataclass
class Constraint:
    sequence: List[NaturalClass]

    def __str__(self) -> str:
        result = "*"
        for nc in self.sequence:
            result += str(nc)
        return result


def parse_constraint(query: str) -> Constraint:
    assert query[0] == '*'
    sequence = []
    for m in re.finditer(r"\[(\^?)(.+?)\]", query[1:]):
        entries = []
        complement = m.group(1) == '^'
        for pair in m.group(2).split(','):
            entries.append((pair[1:], pair[0]))
        sequence.append(NaturalClass(entries, complement))
    return Constraint(sequence)
