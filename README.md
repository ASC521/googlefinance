# googlefinance
Python package to scrape relevant data from Google Finance.  This package is able to retrieve the latest quote, historical high, low, close, and open prices between a set of dates, and relevant company news.

# Retrieve Current Price
    from googlefinance import Stock

    aapl = Stock('AAPL')
    aapl.get_quote()
