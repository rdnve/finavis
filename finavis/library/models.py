from __future__ import annotations

import datetime as dt
import typing as ty
from copy import deepcopy
from decimal import Decimal

import attr

from finavis.utils import text_to_decimal


class AbstractModel:
    def to_dict(self) -> ty.Dict[str, str]:
        return deepcopy(self.__dict__)

    @classmethod
    def from_response(cls, raw: ty.Dict[str, ty.Any]) -> ty.Any:
        raise NotImplemented


@attr.s(auto_attribs=True)
class Quote(AbstractModel):
    """
    Model of quote.

    :param str ticker: Ticker name
    :param str company: Company name
    :param str website: Company website
    :param str sector: Name of sector
    :param str industry: Name of industry
    :param str country: Country
    :param str exchange: Exchange
    :param ty.Tuple[str, ...] index: Major index membership
    :param Decimal p_e: Price-to-Earnings (ttm)
    :param Decimal eps_ttm: Diluted EPS (ttm)
    :param Decimal insider_own: Insider ownership
    :param Decimal shs_outstand: Shares outstanding
    :param Decimal perf_week: Performance (Week)
    :param Decimal market_cap: Market capitalization
    :param Decimal forward_p_e: Forward Price-to-Earnings (next fiscal year)
    :param Decimal eps_next_y: EPS estimate for next year
    :param Decimal insider_trans: Insider transactions (6-Month change in Insider Ownership)
    :param Decimal shs_float: Shares float
    :param Decimal perf_month: Performance (Month)
    :param Decimal income: Income (ttm)
    :param Decimal peg: Price-to-Earnings-to-Growth
    :param Decimal eps_next_q: EPS estimate for next quarter
    :param Decimal inst_own: Institutional ownership
    :param str short_float_ratio: Short interest share / ratio
    :param Decimal perf_quarter: Performance (Quarter)
    :param Decimal sales: Revenue (ttm)
    :param Decimal p_s: Price-to-Sales (ttm)
    :param Decimal eps_this_y: EPS growth this year
    :param Decimal inst_trans: Institutional transactions (3-Month change in Institutional Ownership)
    :param Decimal short_interest: Short interest
    :param Decimal perf_half_y: Performance (Half Year)
    :param Decimal book_sh: Book value per share (mrq)
    :param Decimal p_b: Price-to-Book (mrq)
    :param Decimal eps_growth_next_y: EPS growth next year
    :param Decimal roa: Return on Assets (ttm)
    :param Decimal target_price: Analysts' mean target price
    :param Decimal perf_year: Performance (Year)
    :param Decimal cash_sh: Cash per share (mrq)
    :param Decimal p_c: Price to cash per share (mrq)
    :param Decimal eps_next_5y: Long term annual growth estimate (5 years)
    :param Decimal roe: Return on Equity (ttm)
    :param str ttm_range: 52-Week trading range
    :param Decimal perf_ytd: Performance (Year To Date)
    :param Decimal dividend: Dividend (Fiscal Year Estimate)
    :param Decimal p_fcf: Price to Free Cash Flow (ttm)
    :param Decimal eps_past_5y: Annual EPS growth past 5 years
    :param Decimal roi: Return on Investment (ttm)
    :param Decimal ttm_high: Distance from 52-Week High
    :param Decimal beta: Beta
    :param Decimal dividend_percent: Dividend yield (Fiscal Year Estimate)
    :param Decimal quick_ratio: Quick Ratio (mrq)
    :param Decimal sales_past_5y: Annual sales growth past 5 years
    :param Decimal gross_margin: Gross Margin (ttm)
    :param Decimal ttm_low: Distance from 52-Week Low
    :param Decimal atr: Average True Range (14)
    :param Decimal employees: Full time employees
    :param Decimal current_ratio: Current Ratio (mrq)
    :param Decimal sales_q_q: Quarterly revenue growth (YoY)
    :param Decimal oper_margin: Operating Margin (ttm)
    :param Decimal rsi_14: Relative Strength Index
    :param str volatility_w: Volatility in week
    :param str volatility_m: Volatility in month
    :param bool is_optionable: Stock has options trading on a market exchange
    :param Decimal debt_eq: Total Debt to Equity (mrq)
    :param Decimal eps_q_q: Quarterly earnings growth (YoY)
    :param Decimal profit_margin: Net Profit Margin (ttm)
    :param Decimal rel_volume: Relative volume
    :param Decimal prev_close: Previous close
    :param bool is_shortable: Stock available to sell short
    :param Decimal lt_debt_eq: Long Term Debt to Equity (mrq)
    :param dt.date earnings_at: Earnings date
    :param str earnings_market: BMO = Before Market Open, AMC = After Market Close
    :param Decimal payout: Dividend Payout Ratio (ttm)
    :param Decimal avg_volume: Average volume (3 month)
    :param Decimal price: Current stock price
    :param Decimal recom: Analysts' mean recommendation (1=Buy 5=Sell)
    :param Decimal sma20: Distance from 20-Day Simple Moving Average
    :param Decimal sma50: Distance from 50-Day Simple Moving Average
    :param Decimal sma200: Distance from 200-Day Simple Moving Average
    :param Decimal volume: Volume
    :param Decimal change: Performance (today)
    """

    ticker: str
    company: str
    website: str
    sector: str
    industry: str
    country: str
    exchange: str
    p_e: Decimal
    eps_ttm: Decimal
    insider_own: Decimal
    shs_outstand: Decimal
    perf_week: Decimal
    market_cap: Decimal
    forward_p_e: Decimal
    eps_next_y: Decimal
    insider_trans: Decimal
    shs_float: Decimal
    perf_month: Decimal
    income: Decimal
    peg: Decimal
    eps_next_q: Decimal
    inst_own: Decimal
    short_float_ratio: str
    perf_quarter: Decimal
    sales: Decimal
    p_s: Decimal
    eps_this_y: Decimal
    inst_trans: Decimal
    short_interest: Decimal
    perf_half_y: Decimal
    book_sh: Decimal
    p_b: Decimal
    eps_growth_next_y: Decimal
    roa: Decimal
    target_price: Decimal
    perf_year: Decimal
    cash_sh: Decimal
    p_c: Decimal
    eps_next_5y: Decimal
    roe: Decimal
    ttm_range: str
    perf_ytd: Decimal
    dividend: Decimal
    p_fcf: Decimal
    eps_past_5y: Decimal
    roi: Decimal
    ttm_high: Decimal
    beta: Decimal
    dividend_percent: Decimal
    quick_ratio: Decimal
    sales_past_5y: Decimal
    gross_margin: Decimal
    ttm_low: Decimal
    atr: Decimal
    employees: Decimal
    current_ratio: Decimal
    sales_q_q: Decimal
    oper_margin: Decimal
    rsi_14: Decimal
    volatility_w: Decimal
    volatility_m: Decimal
    is_optionable: bool
    debt_eq: Decimal
    eps_q_q: Decimal
    profit_margin: Decimal
    rel_volume: Decimal
    prev_close: Decimal
    is_shortable: bool
    lt_debt_eq: Decimal
    earnings_market: str
    payout: Decimal
    avg_volume: Decimal
    price: Decimal
    recom: Decimal
    sma20: Decimal
    sma50: Decimal
    sma200: Decimal
    volume: Decimal
    change: Decimal
    index: ty.Optional[ty.Tuple[str, ...]] = None
    earnings_at: ty.Optional[dt.date] = None

    def to_dict(self) -> ty.Dict[str, str]:
        raw: ty.Dict[str, str] = super().to_dict()
        for key, value in self.__dict__.items():
            if key.startswith("ttm_"):
                raw["52w_" + key.split("ttm_")[-1]] = value
        return raw

    @classmethod
    def from_response(cls, raw: ty.Dict[str, ty.Any]) -> Quote:
        """Make class from raw_data"""

        data: ty.Dict[str, ty.Any] = dict()

        index = raw.pop("index", None)
        if isinstance(index, str):
            data.update(index=tuple((x.strip() for x in index.split(","))))

        optionable = raw.pop("optionable", None)
        if optionable is not None:
            data.update(is_optionable=optionable == "Yes")

        shortable = raw.pop("shortable", None)
        if shortable is not None:
            data.update(is_shortable=shortable == "Yes")

        earnings = raw.pop("earnings", None)
        if isinstance(earnings, str):
            data.update(earnings_market=earnings.split()[-1])

            today = dt.date.today()
            earn_at = dt.datetime.strptime(
                " ".join([str(today.year)] + earnings.split()[0:2]), "%Y %b %d"
            ).date()
            if earn_at < today:
                earn_at = dt.date(today.year + 1, earn_at.month, earn_at.day)

            data.update(earnings_at=earn_at)

        volatility = raw.pop("volatility", None)
        if isinstance(volatility, str):
            volatility_w, volatility_m = volatility.split()
            if isinstance(volatility_w, str):
                data.update(volatility_w=Decimal(volatility_w.split("%")[0]))
            if isinstance(volatility_m, str):
                data.update(volatility_m=Decimal(volatility_m.split("%")[0]))

        for field_name, field_type in cls.__annotations__.items():
            value: ty.Any = raw.get(field_name)

            if field_name in data.keys():
                continue

            if field_type == "str":
                data[field_name] = value
                continue

            if field_type == "Decimal":
                if value is None:
                    data[field_name] = value
                    continue

                if value.endswith(("M", "B")):
                    data[field_name] = text_to_decimal(value=value)
                    continue

                if value.endswith("%"):
                    data[field_name] = Decimal(value.split("%")[0])
                    continue

                if "," in value:
                    value = value.replace(",", "")

                data[field_name] = Decimal(value)

        return cls(**data)


@attr.s(auto_attribs=True)
class Overview(AbstractModel):
    """
    Model of overview table in screener.

    :param str ticker: Ticker
    :param str company: Company
    :param str sector: Sector
    :param str industry: Industry
    :param str country: Country
    :param str market_cap: Market capitalization
    :param str p_e: Price-to-Earnings (ttm)
    :param str price: Current stock price
    :param str change: Performance (today)
    :param str volume: Volume
    """

    ticker: str
    company: str
    sector: str
    industry: str
    country: str
    market_cap: str
    p_e: str
    price: str
    change: str
    volume: str
