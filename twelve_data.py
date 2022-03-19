from twelvedata import TDClient

API_KEY = "056f9e830b1e4dc18f68149d53bb8c45"

class TwelveData:
    def __init__(self):
        pass

    def get_all_data(self, ticker):
        time_series = TDClient(apikey=API_KEY).time_series(
            symbol=ticker,
            interval="1day",
            outputsize=5000,
            timezone="America/New_York",
        )
        return list(time_series.as_json())

    def get_specific_data(self, ticker, specific_data):
        dataset = self.get_all_data(ticker)
        return [float(val[specific_data]) for val in dataset]

#https://api.twelvedata.com/dividends?symbol=AAPL&apikey=056f9e830b1e4dc18f68149d53bb8c45&range=5y