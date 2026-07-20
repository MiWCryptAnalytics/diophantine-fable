"""Decision objects returned by every solver.

The core discipline of this toolkit: never overclaim. YES carries a verified
witness (or a certified symbolic solution), NO carries a finite re-checkable
reason, and anything short of proof is UNDECIDED with the exhausted bound.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    YES = "YES"
    NO = "NO"
    UNDECIDED = "UNDECIDED"


@dataclass(frozen=True)
class Decision:
    status: Status
    method: str
    certificate: object = None
    detail: str = ""

    def __str__(self) -> str:
        parts = [f"{self.status.value} [{self.method}]"]
        if self.certificate is not None:
            parts.append(f"certificate={self.certificate}")
        if self.detail:
            parts.append(self.detail)
        return "  ".join(parts)


def yes(method: str, witness=None, detail: str = "") -> Decision:
    return Decision(Status.YES, method, witness, detail)


def no(method: str, certificate=None, detail: str = "") -> Decision:
    return Decision(Status.NO, method, certificate, detail)


def undecided(method: str, bound=None, detail: str = "") -> Decision:
    return Decision(Status.UNDECIDED, method, bound, detail)
