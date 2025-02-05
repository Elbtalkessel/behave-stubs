from _typeshed import Incomplete
from typing import Callable, TypeVar
from behave.runner import Context

__all__ = ["given", "when", "then", "step", "Given", "When", "Then", "Step"]

class AmbiguousStep(ValueError): ...

class StepRegistry:
    steps: Incomplete
    def __init__(self) -> None: ...
    @staticmethod
    def same_step_definition(step, other_pattern, other_location): ...
    def add_step_definition(self, keyword, step_text, func) -> None: ...
    def find_step_definition(self, step): ...
    def find_match(self, step): ...
    def make_decorator(self, step_type): ...

StepFunc = TypeVar("StepFunc", bound=Callable[[Context], None])

step = Callable[[StepFunc], StepFunc]
given = step
when = step
then = step
Given = given
When = when
Then = then
Step = step
