from yfs import YahooFinanceScraping

yfs = YahooFinanceScraping('IBM')

regular_market_price = yfs.regular_market_price()
print(regular_market_price)

previous_close = yfs.previous_close()
print(previous_close)

open_value = yfs.open_value()
print(open_value)

days_range = yfs.days_range()
print(days_range)
