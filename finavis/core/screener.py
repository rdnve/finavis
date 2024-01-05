import re
import typing as ty

from finavis.library import Exchange, Index, Order, Overview, Signal, Table
from finavis.utils.sessions import make_request

if ty.TYPE_CHECKING:
    from lxml import html


class Screener:
    """Screen! Screen! Screener!"""

    _args_validate_mapping: ty.Dict[str, ty.Any] = dict(
        exchange=Exchange,
        index=Index,
        signal=Signal,
        table=Table,
        order_by=Order,
    )
    _screener_mapping: ty.Dict[str, ty.Any] = {Table.OVERVIEW.value: Overview}
    _per_pages: int = 20
    _items: ty.List[Overview] = list()

    def __len__(self) -> int:
        """Total objects in array"""

        return len(self._items)

    def __getitem__(self, index):
        """Getting objects by index"""

        return self._items[index]

    def __next__(self):
        for item in self._items:
            yield item

        raise StopIteration

    get = __getitem__

    def __init__(
        self,
        exchange: ty.Optional[ty.Union[Exchange, str]] = None,
        index: ty.Optional[ty.Union[Index, str]] = None,
        signal: ty.Optional[ty.Union[Signal, str]] = None,
        table: ty.Optional[ty.Union[Table, str]] = Table.OVERVIEW,
        order_by: ty.Union[Order, str] = Order.TICKER_ASC,
    ) -> None:
        """Initialization and validation"""

        self.exchange = str(exchange) if exchange is not None else None
        self.index = str(index) if index is not None else None
        self.signal = str(signal) if signal is not None else None
        self.table = str(table) if table is not None else None
        self.order_by = str(order_by) if order_by is not None else None

        for arg_name, arg_choices in self._args_validate_mapping.items():
            value: ty.Optional[str] = getattr(self, arg_name)
            if value is not None and str(value) not in arg_choices:
                raise TypeError(
                    f"arg {arg_name}={value} is not allowed, please select "
                    f"some another, if required: {', '.join(arg_choices.values())}."
                )

        self.filters: ty.List[str] = list(filter(None, [self.exchange, self.index]))

        self.total: int = 0
        self.pages: int = 0

    def __repr__(self) -> str:
        """String representation of class"""

        return (
            f"<{self.__class__.__name__} "
            f"exchange={self.exchange}, index={self.index}, signal={self.signal}, "
            f"table={self.table}, order_by={self.order_by}, total={self.total}, "
            f"pages={self.pages}>"
        )

    def __call__(self) -> ty.List[Overview]:
        if len(self._items) > 0:
            return self._items

        for index, item in enumerate(self._yielding_objects(page=1)):
            self._items.append(item)

        return self._items

    def _yielding_objects(self, page: int = 1) -> ty.Iterable[ty.Union[Overview]]:
        """Getting data and create object"""

        query_params: ty.Dict[str, ty.Any] = dict(
            v=self.table,
            o=self.order_by,
            r=((page * self._per_pages) - self._per_pages) + 1,
        )

        if len(self.filters) > 0:
            query_params.update(f=",".join(self.filters))

        raw: "html.HtmlElement" = make_request(
            path="/screener.ashx",
            query_params=query_params,
        )

        if not self.total:
            try:
                total_raw = raw.get_element_by_id("screener-total")
                total_raw = total_raw.text_content()  # type: ignore
            except IndexError:
                return None
            else:
                total_raw_lines = re.findall(r"\s\d+", str(total_raw))
                if len(total_raw_lines) > 0:
                    self.total = int(total_raw_lines[0].strip())
                    self.pages = self._get_total_pages(
                        total=self.total / self._per_pages
                    )

        if not self.total:
            return None

        try:
            raw = raw.get_element_by_id("screener-table")
        except KeyError:
            return None

        for raw_item in raw.cssselect("tr")[3:]:
            key: str = self._screener_mapping[self.table].__name__.lower()  # type: ignore
            yield getattr(self, f"_get_{key}")(raw=raw_item)

        if page < self.pages:
            yield from self._yielding_objects(page=page + 1)

    @staticmethod
    def _get_overview(raw: "html.HtmlElement") -> Overview:
        """Make overview object"""

        kwargs: ty.Dict[str, str] = dict(
            zip(
                Overview.__annotations__.keys(),
                [x if x != "-" else None for x in raw.xpath("td//text()")[1:]],
            )
        )

        return Overview(**kwargs)

    @staticmethod
    def _get_total_pages(total: float) -> int:
        """Helper func"""

        pages, tail = str(total).split(".")
        return int(pages) + 1 if int(tail) > 0 else int(pages)
