import decimal
import typing as ty
from decimal import InvalidOperation

__all__ = (
    "Decimal",
    "InvalidOperation",
)


class Decimal(decimal.Decimal):
    @classmethod
    def __new__(cls, *args, **kwargs) -> ty.Any:
        try:
            return super().__new__(*args, **kwargs)
        except InvalidOperation as e:
            raise InvalidOperation(f"{e} (check {args=!s})")
