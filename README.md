# googlefinance
Python package to scrape relevant data from Google Finance.  This package is able to retrieve the latest quote, historical high, low, close, and open prices between a set of dates, and relevant company news.

# Example
    from googlefinance import Stock

    aapl = Stock('AAPL')
    quote = aapl.get_quote()

    # Response
    {
        'ID': '22144', 
        'TickerSymbol': 'AAPL', 
        'Exchange': 'NASDAQ', 
        'LastTradePrice': '142.69', 
        'LastTradeDateTime': '2017-06-29T13:07:05Z', 
        'Change': '-3.14', 
        'ChangePercent': '-2.15', 
        'PreviousCloseFix': '145.83'
    }

    hist_prices = aapl.get_historical_prices('4/28/2017', '5/30/2017')

    # Response
    [
        {
            'Date': datetime.datetime(2017, 5, 31, 0, 0), 
            'Open': '153.97', 
            'High': '154.17', 
            'Low': '152.38', 
            'Close': '152.76', 
            'Volume': '24451164'
        }, 
        {
            'Date': datetime.datetime(2017, 5, 30, 0, 0), 
            'Open': '153.42', 
            'High': '154.43', 
            'Low': '153.33', 
            'Close': '153.67', 
            'Volume': '20126851'
        }, 
        {
            'Date': datetime.datetime(2017, 5, 26, 0, 0), 
            'Open': '154.00', 
            'High': '154.24', 
            'Low': '153.31', 
            'Close': '153.61', 
            'Volume': '21927637'
        }, 
        {
            'Date': datetime.datetime(2017, 5, 25, 0, 0), 
            'Open': '153.73', 
            'High': '154.35', 
            'Low': '153.03', 
            'Close': '153.87', 
            'Volume': '19235598'
        }, 
        {
            'Date': datetime.datetime(2017, 5, 24, 0, 0), 
            'Open': '153.84', 
            'High': '154.17', 
            'Low': '152.67', 
            'Close': '153.34', 
            'Volume': '19219154'
        }
    ]

    news = aapl.get_stock_news()

    # Response
    [
        {
            'headline': 'Apple, Inc.: A Competitive DJ Stock Investment\xa0Now?', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://seekingalpha.com/article/4084788-apple-inc-competitive-dj-stock-investment-now&cid=0&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNFH2esB_dtnSFpl3VmP5WF2rk8D1w', 
            'src': 'Seeking Alpha', 
            'date': '4 hours ago'
        }, 
        {
            'headline': "Why This Apple Inc. iPhone 8 Rumor Isn't So\xa0Crazy", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/28/why-this-apple-inc-iphone-8-rumor-isnt-so-crazy.aspx&cid=52779543889650&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNH7zzRcQ5ngF1TqDs5SONA0zcWFfQ', 
            'src': 'Motley Fool', 
            'date': 'Jun 28, 2017'
        }, 
        {
            'headline': "Here's When to Expect Apple Inc.'s New AI\xa0Chip", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/26/heres-when-to-expect-apple-incs-new-ai-chip.aspx&cid=52779542834974&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNHBsp4Ch7OK7biOAnIDSVqwneOXVQ', 
            'src': 'Motley Fool', 
            'date': 'Jun 26, 2017'
        }, 
        {
            'headline': '2 Apple Inc. Product Launches to Look Forward to in\xa02017', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/26/2-apple-inc-product-launches-to-look-forward-to-in.aspx&cid=52779542518593&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNF_pIxPzfvO9ICFwUl8C1NyGjYt2g', 
            'src': 'Motley Fool',
            'date': 'Jun 26, 2017'
        }, 
        {
            'headline': 'Apple, Inc. Scoops Up Another Augmented Reality\xa0Company', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/27/apple-inc-scoops-up-another-augmented-reality-comp.aspx&cid=52779542883517&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNHigE_AOuCFP23sHy2SmErMMZyfAw', 
            'src': 'Motley Fool', 
            'date': 'Jun 27, 2017'
        }, 
        {
            'headline': 'The Apple Inc. (AAPL) iPhone Turns 10\xa0Today', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://investorplace.com/2017/06/apple-inc-s-aapl-iphone-turns-10-today/&cid=52779543733181&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNH724ROQmXX-dhfmZGOBjQ3ZtQ9Qw', 
            'src': 'Investorplace.com', 
            'date': '3 hours ago'
        }, 
        {
            'headline': 'Apple For\xa0Beginners', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://seekingalpha.com/article/4084359-apple-beginners&cid=0&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNE4G0LnK6eF_onrKUj7rs8_p1SmFg',
            'src': 'Seeking Alpha', 
            'date': 'Jun 27, 2017'
        }, 
        {
            'headline': 'Apple Inc. (AAPL) Has Potential to Be the Best of the “A”\xa0Stocks', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://investorplace.com/2017/06/apple-inc-aapl-potential-best-stocks/&cid=52779544125905&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEfEJRBzIiOWpI5alZmZqBRXgcyzA', 
            'src': 'Investorplace.com', 'date': '15 hours ago'
        }, 
        {
            'headline': 'Is Apple, Inc. Hoping to Poach Amazon Alexa\xa0Engineers?', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://host.madison.com/business/investment/markets-and-stocks/is-apple-inc-hoping-to-poach-amazon-alexa-engineers/article_b8dd4dfc-03ee-50c3-ac38-87db80c55f30.html&cid=52779543348814&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEUd0XqTaWBcBn9xYdRd3ZV7j8H4A', 
            'src': 'Madison.com', 
            'date': 'Jun 27, 2017'
        }, 
        {
            'headline': 'Apple Music Might Become More Profitable for Apple,\xa0Inc.', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://host.madison.com/business/investment/markets-and-stocks/apple-music-might-become-more-profitable-for-apple-inc/article_f702878f-9e7e-521d-abee-2e925bed5c8a.html&cid=52779542152797&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNFu6xjSGZNhoKq6PL9IkQmsM8H50w', 
            'src': 'Madison.com', 
            'date': 'Jun 24, 2017'
        }, 
        {
            'headline': "Apple And Augmented Reality: Where's The\xa0Money?", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://seekingalpha.com/article/4084572-apple-augmented-reality-money&cid=52779541582957&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNGGkRLg_zcn9WcxC6Q9mFcm85uOIg', 
            'src': 'Seeking Alpha', 
            'date': 'Jun 28, 2017'
        }, 
        {
            'headline': "Apple's Price Chart Is Entering Into Ugly\xa0Territory", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://seekingalpha.com/article/4084563-apples-price-chart-entering-ugly-territory&cid=0&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNGIoAT5AEbBvZNmplpvaXN56NOanw', 
            'src': 'Seeking Alpha', 
            'date': 'Jun 28, 2017'
        }, 
        {
            'headline': "Apple Inc. Isn't Giving Up on the\xa0iPad", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/19/apple-inc-isnt-giving-up-on-the-ipad.aspx&cid=52779536663879&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEAI2YFblvfDPzGW9jlCaUrUEbISQ', 
            'src': 'Motley Fool', 
            'date': 'Jun 19, 2017'
        }, 
        {
            'headline': 'Apple Inc. Reportedly Still Working Out iPhone 8 Touch ID\xa0Tech', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/22/apple-inc-reportedly-still-working-out-iphone-8-to.aspx&cid=52779537392523&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEu9b7XN1KDPCgs42IQ789kiEM6Lw', 
            'src': 'MotleyFool', 
            'date': 'Jun 22, 2017'
        }, 
        {
            'headline': '3 Apple Inc. Supplier Stocks That Could Benefit From the iPhone\xa08', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/19/3-apple-inc-supplier-stocks-that-could-benefit-fro.aspx&cid=52779535460039&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNHVRfRns-IB7jyZ5pqgouKfONbc8Q', 
            'src': 'Motley Fool', 'date': 'Jun 19, 2017'
        }, 
        {
            'headline': 'Do Apple and Facebook have what it takes to succeed in\xa0TV?', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://www.marketwatch.com/story/do-apple-and-facebook-have-what-it-takes-to-succeed-in-tv-2017-06-27&cid=52779543301332&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEvHROfTrpbS9HuGueFYcBJYRO1GA', 
            'src': 'MarketWatch', 
            'date': 'Jun 27, 2017'
        }, 
        {
            'headline':'3 Big Stock Charts for Wednesday: Chesapeake Energy Corporation (CHK), Apple\xa0...', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://investorplace.com/2017/06/3-big-stock-charts-for-wednesday-chesapeake-energy-corporation-chk-apple-inc-aapl-and-united-states-steel-corporation-x/&cid=52779540893035&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNEvakaSPlYfUtUjlMA0M0CAzLJ9CA', 
            'src': 'Investorplace.com', 
            'date': 'Jun 28, 2017'
        }, 
        {
            'headline': 'Apple, Inc. Has Made Incredible Progress Plugging Supply-Chain\xa0Leaks', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://host.madison.com/business/investment/markets-and-stocks/apple-inc-has-made-incredible-progress-plugging-supply-chain-leaks/article_fcecb9ec-657e-57ca-adbb-e44d8d972e81.html&cid=52779536291341&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNHvpsqeCk4mOsq_91F58uGQwFcOsg', 
            'src': 'Madison.com', 
            'date': 'Jun 21, 2017'
        }, 
        {
            'headline': "I Still Can't Believe Apple Inc. Spent $3 Billion on Beats\xa0Electronics", 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/23/i-still-cant-believe-apple-inc-spent-3-billion-on.aspx&cid=0&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNGUci7-8QQtZvB1bbGfhk_qlZnu4g', 
            'src': 'Motley Fool', 
            'date': 'Jun 23, 2017'
        }, 
        {
            'headline': 'Apple Inc. Supplier Puts Itself Up for\xa0Sale', 
            'url': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.fool.com/investing/2017/06/22/apple-inc-supplier-puts-itself-up-for-sale.aspx&cid=52779537802828&ei=DjVVWfH3O8WumAGQ4pOICw&usg=AFQjCNFMixm_6aVGWKMAG26--jWqBo5stA', 
            'src': 'Motley Fool',
            'date': 'Jun 22, 2017'
        }
    ]