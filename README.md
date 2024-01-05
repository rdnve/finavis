## another unofficial api for [finviz.com](https://finviz.com)

[![python-latest](https://img.shields.io/pypi/pyversions/finavis?logo=python&logoColor=FFE873)](https://www.python.org/downloads/)
[![pypi](https://img.shields.io/badge/pypi-0.0.29-blue?logo=pypi&logoColor=FFE873)](https://pypi.org/project/finavis/)
[![pypi_downloads](https://img.shields.io/pypi/dm/finavis)](https://pypi.org/project/finavis/)
[![license](https://img.shields.io/pypi/l/finavis)](https://github.com/rdnve/finavis/blob/master/LICENSE)


### installation

```bash
# via pypi (recommended)
$ python -m pip install -U finavis

# or using github w/ pip
$ python -m pip install git+https://github.com/rdnve/finavis.git

# or using github w/ poetry
$ poetry add git+https://github.com/rdnve/finavis.git
```

### getting a single quote
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

### getting a several quotes
```python
import typing as ty

from finavis import get_quotes

tickers: ty.Tuple[str, ...] = ("AAPL", "INTC", "QCOM")
for quote in get_quotes(tickers=tickers):
    print(f"Ticker: {quote.ticker}, price: {quote.price}, w/ EPS {quote.eps_ttm}")
```

### getting a screener w/ objects
```python
from finavis import Screener
from finavis.library import Exchange, Index, Order

screener: Screener = Screener(
    exchange=Exchange.NASDAQ,
    index=Index.SP500,
    order_by=Order.CHANGE_ASC,
)

for index, overview in enumerate(screener()):
    print(f"Ticker: {overview.ticker}, price: {overview.price} - change: {overview.change}")
```

### disclaimer
using this library to acquire data from some website is against their "terms of service" and *robots.txt*; use it responsibly and at your own risk, this library was built purely for educational purposes.

### important information
any quote data displayed on the [finviz.com](https://finviz.com) website is delayed by 15 minutes for nasdaq/nyse/amex; this api should **NOT be used** for real-time trading, it's primary purpose for research in educational purposes.
