from pandas import DataFrame
from freqtrade.strategy import IStrategy


class XautDryRunStrategy(IStrategy):
    """Deployment smoke-test strategy: intentionally emits no trade signals."""

    INTERFACE_VERSION = 3
    timeframe = "5m"
    can_short = False
    minimal_roi = {"0": 0.10}
    stoploss = -0.05
    startup_candle_count = 30
    process_only_new_candles = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["enter_long"] = 0
        dataframe["enter_tag"] = None
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["exit_long"] = 0
        dataframe["exit_tag"] = None
        return dataframe
