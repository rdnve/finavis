import pytest

from finavis.library.types import Decimal, InvalidOperation


def test_custom_decimal() -> None:
    with pytest.raises(InvalidOperation):
        Decimal("123foo")

    try:
        Decimal("123foo")
    except InvalidOperation as e:
        assert "check args" in str(e)
        assert "123foo" in str(e)
