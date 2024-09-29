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


if __name__ == "__main__":
    # *[^-voice,+anterior,+strident][-approximant]
    print(Constraint([
        NaturalClass([("voice", "-"), ("anterior", "+"), ("strident", "+")], complement=True),
        NaturalClass([("approximant", "-")])
    ]))
