import functools
import typing as ty

from finavis.exception import NotFound
from finavis.library import Quote
from finavis.utils import make_request, text_to_label

if ty.TYPE_CHECKING:
    from lxml.html import HtmlElement


@functools.lru_cache(maxsize=32, typed=False)
def get_quote(ticker: str) -> Quote:
    """Receive info by ticker name"""

    if not isinstance(ticker, str):
        raise TypeError(
            f"Argument `ticker` is not a string (currently: type({type(ticker)}))"
        )

    data: ty.Dict[str, ty.Any] = dict()
    raw: "HtmlElement" = make_request(
        path="/quote.ashx",
        query_params={"t": str(ticker)},
    )

    try:
        title: "HtmlElement" = raw.cssselect('div[class="fv-container py-2.5"]')[0]
    except IndexError:
        raise NotFound(f"{ticker=!s} not found")

    ticker = title.cssselect(
        'h1[class="js-recent-quote-ticker quote-header_ticker-wrapper_ticker"]'
    )[0].text_content()
    data["ticker"] = str(ticker).strip()

    try:
        company = title.cssselect(
            'h2[class="quote-header_ticker-wrapper_company text-xl"]'
        )[0]
    except IndexError:
        company = title.cssselect('h2[class="quote-header_ticker-wrapper_company"]')[0]

    data["company"] = company.text_content().strip()

    website = company.cssselect('a[class="tab-link block truncate"]')[0].attrib["href"]
    if str(website).startswith("http"):
        data["website"] = website

    keys = ["Sector", "Industry", "Country", "Exchange"]
    fields = [f.text_content() for f in title.cssselect('a[class="tab-link"]')]
    data_raw = dict(zip(keys, fields))
    for key, value in data_raw.items():
        data[key.lower()] = value

    for rows in raw.cssselect('tr[class="table-dark-row"]'):
        rows = rows.xpath("td")
        for index in range(0, 11, 2):
            field_label, field_data = rows[index], rows[index + 1]

            name: str = field_label.text_content().strip()
            label: str = ty.cast(str, text_to_label(value=name))
            if label in data.keys() and name == "EPS next Y":
                name = "EPS growth next Y"
                label = ty.cast(str, text_to_label(value=name))

            value = field_data.text_content().strip()  # type: ignore
            if value == "-":
                value = None  # type: ignore

            data[label] = value

    return Quote(**data)
