from dataclasses import dataclass

from e import E


@dataclass
class If:
    e: E
    if_true: list
    if_false: list
    