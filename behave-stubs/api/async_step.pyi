from _typeshed import Incomplete
from typing import Callable, Optional, TypeVar, Awaitable, overload

R = TypeVar("R")

@overload
def async_run_until_complete(
    astep_func: Callable[..., Awaitable[R]]
) -> Callable[..., R]:
    ...

@overload
def async_run_until_complete(
    *,
    loop: Optional[Incomplete] = None,
    timeout: Optional[float] = None,
    async_context: Optional[str] = None,
    should_close: bool = False
) -> Callable[[Callable[..., Awaitable[R]]], Callable[..., R]]:
    ...

def async_run_until_complete(
    astep_func: Optional[Callable[..., Awaitable[R]]] = None,
    *,
    loop: Optional[Incomplete] = None,
    timeout: Optional[float] = None,
    async_context: Optional[str] = None,
    should_close: bool = False
) -> Callable[..., R] | Callable[[Callable[..., Awaitable[R]]], Callable[..., R]]:
    ...

has_asyncio: bool

run_until_complete = async_run_until_complete

class AsyncContext:
    default_name: str
    loop: Incomplete
    tasks: Incomplete
    name: Incomplete
    should_close: Incomplete
    def __init__(
        self,
        loop: Incomplete | None = None,
        name: Incomplete | None = None,
        should_close: bool = False,
        tasks: Incomplete | None = None,
    ) -> None: ...
    def __del__(self) -> None: ...
    def close(self) -> None: ...

def use_or_create_async_context(
    context, name: Incomplete | None = None, loop: Incomplete | None = None, **kwargs
): ...
