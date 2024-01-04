## another unofficial api for [finviz.com](https://finviz.com)

[![python3120](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![poetry](https://img.shields.io/badge/poetry-1.4.2-blue.svg)](https://github.com/python-poetry/poetry/releases/tag/1.4.2/)
[![pypi](https://badge.fury.io/py/finavis.svg?t=1704406095)](https://pypi.org/project/finavis/)```bash
$ python -m pip install -U finavis
```

### getting a quote
```python
import typing as ty

from finavis import get_quote
from finavis.library import Quote

quote: Quote = get_quote(ticker="AAPL")

# accessing to attributes: type help(quote) for more
print(f"Ticker: {quote.ticker}, price: {quote.price}, w/ EPS {quote.eps_ttm}")

# extract attributes to dictionary
data: ty.Dict[str, str] = quote.to_dict()
```

### getting a screener w/ objects
```python
from finavis import Screener
from finavis.library import ExchangeChoices, IndexChoices, OrderChoices

screener: Screener = Screener(
    exchange=ExchangeChoices.NASDAQ,
    index=IndexChoices.SP500,
    order_by=OrderChoices.CHANGE_ASC,
)

for index, overview in enumerate(screener()):
    print(f"Ticker: {overview.ticker}, price: {overview.price} - change: {overview.change}")
```

### disclaimer
using this library to acquire data from some website is against their "terms of service" and *robots.txt*; use it responsibly and at your own risk, this library was built purely for educational purposes.


### important information
any quote data displayed on the [finviz.com](https://finviz.com) website is delayed by 15 minutes for nasdaq and 20 minutes for nyse/amex; this api should **NOT be used** for real-time trading, it's primary purpose for research in educational purposes.
