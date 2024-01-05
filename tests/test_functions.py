import typing as ty

import pytest

from finavis.library.types import Decimal, InvalidOperation
from finavis.utils import text_to_decimal, text_to_label


def test_text_to_decimal_millions() -> None:
    res: Decimal = text_to_decimal("10M")

    assert isinstance(res, Decimal)
    assert res == Decimal("10000000")


def test_text_to_decimal_billions() -> None:
    res: Decimal = text_to_decimal("10B")

    assert isinstance(res, Decimal)
    assert res == Decimal("10000000000")


def test_text_to_decimal_raises() -> None:
    with pytest.raises(InvalidOperation):
        text_to_decimal("foo")


def test_text_to_decimal_none_type() -> None:
    res: ty.Optional[Decimal] = text_to_decimal(value=None)
    assert isinstance(res, type(None))


def test_text_to_label() -> None:
    res: str = text_to_label("Hello world")
    assert isinstance(res, str)
    assert res == "hello_world"

    res: ty.Optional[str] = text_to_label(value="P/E in %")
    assert isinstance(res, str)
    assert res == "p_e_in_percent"

    res: ty.Optional[str] = text_to_label(value="52W in %")
    assert isinstance(res, str)
    assert res == "ttm_in_percent"

    res: ty.Optional[str] = text_to_label(value="%! foo %")
    assert isinstance(res, str)
    assert res == "percent_foo_percent"
