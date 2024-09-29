"""
0	*[+continuant,+voice,-anterior]	(tier=default)	weight=	5.644087623006924
1	*[+sonorant,+dorsal]	(tier=default)	weight=	5.361312634486015
2	*[^-voice,+anterior,+strident][-approximant]	(tier=default)	weight=	10.303216754356292
"""

from dataclasses import dataclass
from typing import List, Tuple

from phoncon.constraints import Constraint


@dataclass
class Grammar:
    # TODO: maybe tier could be added
    entries: List[Tuple[Constraint, float]]  # (<constraint>, <weight>)
