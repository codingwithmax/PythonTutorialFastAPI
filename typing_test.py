from typing import Union, Optional, Tuple


def division(a: int, b: Optional[int]) -> Union[int, float, None]:
    if b is None:
        return a
    if b != 0:
        return a / b

    return None


def test_unpack(input_val: list[str], index: int) -> tuple[str, int]:
    return input_val[index], index


def untyped_function(a):
    return a


return_val = division(1, 2)
print(return_val)

return_val = division(1, 0)
print(return_val)

return_val_2 = test_unpack(["val_1"], 0)
print(return_val_2)
