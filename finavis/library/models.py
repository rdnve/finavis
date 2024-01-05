import typing as ty
from copy import deepcopy

import attr


class AbstractModel:
    def to_dict(self) -> ty.Dict[str, str]:
        return deepcopy(self.__dict__)


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
    :param str index: Major index membership
    :param str p_e: Price-to-Earnings (ttm)
    :param str eps_ttm: Diluted EPS (ttm)
    :param str insider_own: Insider ownership
    :param str shs_outstand: Shares outstanding
    :param str perf_week: Performance (Week)
    :param str market_cap: Market capitalization
    :param str forward_p_e: Forward Price-to-Earnings (next fiscal year)
    :param str eps_next_y: EPS estimate for next year
    :param str insider_trans: Insider transactions (6-Month change in Insider Ownership)
    :param str shs_float: Shares float
    :param str perf_month: Performance (Month)
    :param str income: Income (ttm)
    :param str peg: Price-to-Earnings-to-Growth
    :param str eps_next_q: EPS estimate for next quarter
    :param str inst_own: Institutional ownership
    :param str short_float_ratio: Short interest share / ratio
    :param str perf_quarter: Performance (Quarter)
    :param str sales: Revenue (ttm)
    :param str p_s: Price-to-Sales (ttm)
    :param str eps_this_y: EPS growth this year
    :param str inst_trans: Institutional transactions (3-Month change in Institutional Ownership)
    :param str short_interest: Short interest
    :param str perf_half_y: Performance (Half Year)
    :param str book_sh: Book value per share (mrq)
    :param str p_b: Price-to-Book (mrq)
    :param str eps_growth_next_y: EPS growth next year
    :param str roa: Return on Assets (ttm)
    :param str target_price: Analysts' mean target price
    :param str perf_year: Performance (Year)
    :param str cash_sh: Cash per share (mrq)
    :param str p_c: Price to cash per share (mrq)
    :param str eps_next_5y: Long term annual growth estimate (5 years)
    :param str roe: Return on Equity (ttm)
    :param str ttm_range: 52-Week trading range
    :param str perf_ytd: Performance (Year To Date)
    :param str dividend: Dividend (Fiscal Year Estimate)
    :param str p_fcf: Price to Free Cash Flow (ttm)
    :param str eps_past_5y: Annual EPS growth past 5 years
    :param str roi: Return on Investment (ttm)
    :param str ttm_high: Distance from 52-Week High
    :param str beta: Beta
    :param str dividend_percent: Dividend yield (Fiscal Year Estimate)
    :param str quick_ratio: Quick Ratio (mrq)
    :param str sales_past_5y: Annual sales growth past 5 years
    :param str gross_margin: Gross Margin (ttm)
    :param str ttm_low: Distance from 52-Week Low
    :param str atr: Average True Range (14)
    :param str employees: Full time employees
    :param str current_ratio: Current Ratio (mrq)
    :param str sales_q_q: Quarterly revenue growth (YoY)
    :param str oper_margin: Operating Margin (ttm)
    :param str rsi_14: Relative Strength Index
    :param str volatility: Volatility (Week, Month)
    :param str optionable: Stock has options trading on a market exchange
    :param str debt_eq: Total Debt to Equity (mrq)
    :param str eps_q_q: Quarterly earnings growth (YoY)
    :param str profit_margin: Net Profit Margin (ttm)
    :param str rel_volume: Relative volume
    :param str prev_close: Previous close
    :param str shortable: Stock available to sell short
    :param str lt_debt_eq: Long Term Debt to Equity (mrq)
    :param str earnings: Earnings date, BMO = Before Market Open, AMC = After Market Close
    :param str payout: Dividend Payout Ratio (ttm)
    :param str avg_volume: Average volume (3 month)
    :param str price: Current stock price
    :param str recom: Analysts' mean recommendation (1=Buy 5=Sell)
    :param str sma20: Distance from 20-Day Simple Moving Average
    :param str sma50: Distance from 50-Day Simple Moving Average
    :param str sma200: Distance from 200-Day Simple Moving Average
    :param str volume: Volume
    :param str change: Performance (today)
    """

    ticker: str
    company: str
    website: str
    sector: str
    industry: str
    country: str
    exchange: str
    index: str
    p_e: str
    eps_ttm: str
    insider_own: str
    shs_outstand: str
    perf_week: str
    market_cap: str
    forward_p_e: str
    eps_next_y: str
    insider_trans: str
    shs_float: str
    perf_month: str
    income: str
    peg: str
    eps_next_q: str
    inst_own: str
    short_float_ratio: str
    perf_quarter: str
    sales: str
    p_s: str
    eps_this_y: str
    inst_trans: str
    short_interest: str
    perf_half_y: str
    book_sh: str
    p_b: str
    eps_growth_next_y: str
    roa: str
    target_price: str
    perf_year: str
    cash_sh: str
    p_c: str
    eps_next_5y: str
    roe: str
    ttm_range: str
    perf_ytd: str
    dividend: str
    p_fcf: str
    eps_past_5y: str
    roi: str
    ttm_high: str
    beta: str
    dividend_percent: str
    quick_ratio: str
    sales_past_5y: str
    gross_margin: str
    ttm_low: str
    atr: str
    employees: str
    current_ratio: str
    sales_q_q: str
    oper_margin: str
    rsi_14: str
    volatility: str
    optionable: str
    debt_eq: str
    eps_q_q: str
    profit_margin: str
    rel_volume: str
    prev_close: str
    shortable: str
    lt_debt_eq: str
    earnings: str
    payout: str
    avg_volume: str
    price: str
    recom: str
    sma20: str
    sma50: str
    sma200: str
    volume: str
    change: str

    def to_dict(self) -> ty.Dict[str, str]:
        raw: ty.Dict[str, str] = super().to_dict()
        for key, value in self.__dict__.items():
            if key.startswith("ttm_"):
                raw["52w_" + key.split("ttm_")[-1]] = value
        return raw


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
