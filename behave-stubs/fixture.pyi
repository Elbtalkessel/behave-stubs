from typing import Callable, TypeVar, Any
from behave.runner import Context

F = TypeVar("F", bound=Callable)

def iscoroutinefunction(func): ...
def is_context_manager(func): ...

class InvalidFixtureError(RuntimeError): ...

def use_fixture(
    # I'd constraint to a function with Context as the first arg, but
    # it seems the function doesn't care about signature.
    fixture_func: Callable[[Any], Any],
    context: Context,
    *fixture_args,
    **fixture_kwargs,
): ...
def use_fixture_by_tag(tag, context, fixture_registry): ...
def fixture_call_params(fixture_func, *args, **kwargs): ...
def use_composite_fixture_with(context, fixture_funcs_with_params): ...
def fixture(
    func: F,
    name: str | None = None,
    pattern: str | None = None,
): F
