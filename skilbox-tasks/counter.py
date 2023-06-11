from typing import Callable, Any
import functools


def counter(func: Callable) -> Any:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.count} раз(а)")
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper


@counter
def my_function(x, y):
    return x * y


print(my_function(5, 6))
print(my_function(7, 8))