from typing import Callable, TypeVar, Any, Coroutine, Awaitable, overload
from behave.runner import Context

F = TypeVar("F", bound=Callable)

def iscoroutinefunction(func): ...
def is_context_manager(func): ...

class InvalidFixtureError(RuntimeError): ...

R = TypeVar("R")

@overload
def use_fixture(
    fixture_func: Callable[[Context], Awaitable[R]],
    context: Context,
    *fixture_args,
    **fixture_kwargs,
) -> Coroutine[Any, Any, R]: ...

@overload
def use_fixture(
    fixture_func: Callable[[Context], R],
    context: Context,
    *fixture_args,
    **fixture_kwargs,
) -> R: ...

def use_fixture_by_tag(tag, context, fixture_registry): ...
def fixture_call_params(fixture_func, *args, **kwargs): ...
def use_composite_fixture_with(context, fixture_funcs_with_params): ...
def fixture(
    func: F,
    name: str | None = None,
    pattern: str | None = None,
): F
