import math
import re
import string
import typing as ty


def intspace(value: ty.Union[int, float, str]) -> str:
    """Separate value by whitespace"""

    original = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r"\g<1> \g<2>", original)

    if original == new:
        return new
    else:
        return intspace(value=new)


def roundd(n: ty.Union[int, float], decimals: int = 0) -> float:
    """Normal round of float"""

    expo_n = n * 10**decimals
    if abs(expo_n) - abs(math.floor(expo_n)) < 0.5:
        return math.floor(expo_n) / 10**decimals

    return math.ceil(expo_n) / 10**decimals


def text_to_label(value: str) -> ty.Optional[str]:
    """Some `Hello world` convert to `hello_world`"""

    result: ty.List[str] = list()

    keys: ty.Set[str] = set(list(string.ascii_lowercase) + list(string.digits))
    for key in value.strip().lower():
        if key == "%":
            result.append("percent")
            continue
        if key in keys:
            result.append(key)
        else:
            if len(result) == 0:
                result.append("_")
            elif "_" != result[-1]:
                result.append("_")

    if len(result) == 0:
        return None
    else:
        line: str = "".join(result)

    if line.startswith("_"):
        line = line[1 : len(line)]

    if line.endswith("_"):
        line = line[0 : len(line) - 1]

    if line.startswith("52w"):
        line = line.replace("52w", "ttm")

    return line
