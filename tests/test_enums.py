from finavis.library import Exchange, Index, Order, Signal, Table


def test_enums_check_existing_method_keys() -> None:
    for klass in [Exchange, Index, Table, Order, Signal]:
        assert getattr(klass, "keys")()
        assert len(getattr(klass, "keys")()) > 0
        assert isinstance(getattr(klass, "keys")(), tuple)


def test_enums_check_existing_method_values() -> None:
    for klass in [Exchange, Index, Table, Order, Signal]:
        assert getattr(klass, "values")()
        assert len(getattr(klass, "values")()) > 0
        assert isinstance(getattr(klass, "values")(), tuple)


def test_enums_summary() -> None:
    """Needed for check only key == str"""

    assert str(Exchange.NASDAQ) == "exch_nasd"
    assert str(Index.SP500) == "idx_sp500"
    assert str(Table.OVERVIEW) == "111"
    assert str(Order.COMPANY_ASC) == "company"
    assert str(Signal.NEW_HIGH) == "ta_newhigh"
