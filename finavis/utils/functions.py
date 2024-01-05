import string
import typing as ty
from decimal import Decimal


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


def text_to_decimal(value: str) -> ty.Optional[Decimal]:
    """Helper func"""

    if value is None:
        return None

    mapp = {
        "M": Decimal("1000000"),
        "B": Decimal("1000000000"),
    }

    sym: str = value[-1]
    return Decimal(str(int(Decimal(value.split(sym)[0]) * mapp[sym])))
