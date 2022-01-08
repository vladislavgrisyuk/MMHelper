from typing import Any


def isFloat(element: Any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def isNumberCorrect(val) -> bool:
    if float(val) > 0 and float(val) < 9999999999:
        return True
    else:
        return False
