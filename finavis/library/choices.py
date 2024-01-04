import typing as ty
from enum import Enum


class EnumChoices(Enum):
    @classmethod
    def values(cls) -> ty.Tuple[str, ...]:
        return tuple(map(lambda c: c.value, cls))


class ExchangeChoices(EnumChoices):
    AMEX = "exch_amex"
    NASDAQ = "exch_nasd"
    NYSE = "exch_nyse"


class IndexChoices(EnumChoices):
    SP500 = "idx_sp500"
    NASDAQ100 = "idx_ndx"
    DJIA = "idx_dji"
    RUSSELL2000 = "idx_rut"


class OrderChoices(EnumChoices):
    TICKER_ASC = "ticker"
    TICKER_DESC = "-ticker"
    COMPANY_ASC = "company"
    COMPANY_DESC = "-company"
    SECTOR_ASC = "sector"
    SECTOR_DESC = "-sector"
    INDUSTRY_ASC = "industry"
    INDUSTRY_DESC = "-industry"
    COUNTRY_ASC = "country"
    COUNTRY_DESC = "-country"
    MARKETCAP_ASC = "marketcap"
    MARKETCAP_DESC = "-marketcap"
    PE_ASC = "pe"
    PE_DESC = "-pe"
    PRICE_ASC = "price"
    PRICE_DESC = "-price"
    CHANGE_ASC = "change"
    CHANGE_DESC = "-change"
    VOLUME_ASC = "volume"
    VOLUME_DESC = "-volume"


class SignalChoices(EnumChoices):
    TOP_GAINERS = "ta_topgainers"
    TOP_LOSERS = "ta_toplosers"
    NEW_HIGH = "ta_newhigh"
    NEW_LOW = "ta_newlow"
    MOST_VOLATILE = "ta_mostvolatile"
    MOST_ACTIVE = "ta_mostactive"
    UNUSUAL_VOLUME = "ta_unusualvolume"
    OVERBOUGHT = "ta_overbought"
    OVERSOLD = "ta_oversold"
    DOWNGRADES = "n_downgrades"
    UPGRADES = "n_upgrades"
    EARNINGS_BEFORE = "n_earningsbefore"
    EARNINGS_AFTER = "n_earningsafter"
    RECENT_INSIDER_BUYING = "it_latestbuys"
    RECENT_INSIDER_SELLING = "it_latestsales"
    MAJOR_NEWS = "n_majornews"
    HORIZONTAL_SR = "ta_p_horizontal"
    TL_RESISTANCE = "ta_p_tlresistance"
    TL_SUPPORT = "ta_p_tlsupport"
    WEDGE_UP = "ta_p_wedgeup"
    WEDGE_DOWN = "ta_p_wedgedown"
    TRIANGLE_ASC = "ta_p_wedgeresistance"
    TRIANGLE_DESC = "ta_p_wedgesupport"
    WEDGE = "ta_p_wedge"
    CHANNEL_UP = "ta_p_channelup"
    CHANNEL_DOWN = "ta_p_channeldown"
    CHANNEL = "ta_p_channel"
    DOUBLE_TOP = "ta_p_doubletop"
    DOUBLE_BOTTOM = "ta_p_doublebottom"
    MULTIPLE_TOP = "ta_p_multipletop"
    MULTIPLE_BOTTOM = "ta_p_multiplebottom"
    HEAD_AND_SHOULDERS = "ta_p_headandshoulders"
    HEAD_AND_SHOULDERS_INVERSE = "ta_p_headandshouldersinv"


class TableChoices(EnumChoices):
    OVERVIEW = "111"
