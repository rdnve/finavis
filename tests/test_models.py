import datetime as dt

from finavis.library.models import Quote
from finavis.library.types import Decimal

from .indexes import EXAMPLE_QUOTE_RAW


def test_quote_building_from_raw_data() -> None:
    quote = Quote.from_response(raw=EXAMPLE_QUOTE_RAW)

    assert isinstance(quote, Quote)
    assert isinstance(quote.index, tuple)
    assert len(quote.index) == 3
    assert quote.ticker == "AAPL"
    assert isinstance(quote.p_e, Decimal)
    assert quote.p_e == Decimal("29.62")
    assert quote.earnings_market == "AMC"
    assert isinstance(quote.earnings_at, dt.date)
    assert quote.earnings_at.isoformat() == "2024-11-02"
    assert isinstance(quote.is_shortable, bool)
    assert quote.is_shortable is True
    assert isinstance(quote.is_optionable, bool)
    assert quote.is_optionable is True
    assert quote.volume == Decimal("27070101")
    assert getattr(quote, "to_dict")()
    assert isinstance(quote.to_dict(), dict)
    assert "52w_high" in quote.to_dict()
    assert quote.to_dict()["52w_high"] == quote.ttm_high
    assert quote.is_filled is True
