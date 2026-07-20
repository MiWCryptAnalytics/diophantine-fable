"""smale5: a toolkit for exploring Smale's 5th problem —
deciding whether f(x,y) = 0 (f ∈ ℤ[u,v]) has an integer solution."""
from .decision import Decision, Status
from .poly import parse, normalize, size, is_solution
from .classify import classify, Component
from .solvers.pipeline import decide

__all__ = ["Decision", "Status", "parse", "normalize", "size", "is_solution",
           "classify", "Component", "decide"]
