from typing import TypeVar
from .base import TaskMiddleware

TaskMiddlewareType = TypeVar(
    "TaskMiddlewareType", bound=TaskMiddleware
)
