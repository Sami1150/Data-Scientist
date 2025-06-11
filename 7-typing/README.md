# Typing Hints

```
x: str = 1

def add(a: int, b: int, c: int) -> int:
    return a+b+c

from typing import List
x: List[List[int]] = [[1, 2, 3], []]

from typing import Dict
x: Dict[str, str] = {"a":"b"}

from typing import Set
x: Set[str] = {"a", "b"}

from typing import Optional
def foo(output: Optional[bool]=False)
    pass

# accepts anything
from typing import Any
def foo(output: Any):
    pass

x: tuple = {1, 2, "abc" } # does not make sure what is inside it

from typing import Tuple
x: Tuple[int, int, int] = {1, 2, 3} # Specify each single element

from typing import Callable

def add(x:int, y: int) -> int:
    return x+y

def foo(func: Callable[[int, int], int]) -> None:
    func(1,2)

foo(add)

```

## Static Code Analysis
1. pip install mypy
2. Use cmd: `mypy Desktop/test.py`

## Resources
1. https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
2. 