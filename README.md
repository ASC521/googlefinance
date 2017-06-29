# googlefinance
Python package to scrape relevant data from Google Finance.  This package is able to retrieve the latest quote, historical high, low, close, and open prices between a set of dates, and relevant company news.

# Example
    from googlefinance import Stock

    aapl = Stock('AAPL')
    quote = aapl.get_quote()

    hist_prices = aapl.get_historical_prices('5/30/2017', '6/30/2017')

    news = aaple.get_stock_news()