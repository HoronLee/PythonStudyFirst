name = "皓月互联"
stock_price = 1145.14
stock_code = "6"
stock_price_daily_growth_factor = 1.91981
growth_days = 7
print(f"{name},股票代码：{stock_code},当前股票{stock_price}")
print("每日增长系数是：%f"%stock_price_daily_growth_factor,"经过%d的增长之后"%growth_days,"股价达到：%.2f"%(stock_price*stock_price_daily_growth_factor**growth_days))