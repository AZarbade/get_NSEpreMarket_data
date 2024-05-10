import pandas as pd
from nsepython import nse_eq, fnolist, nse_eq_symbols

print(fnolist())

# symbols = pd.read_csv("pre_market_extract/symbol_lists/nifty_50.csv", header=None)[0]
#
# full_data = {}
# for symbol in symbols:
#     try:
#         print(f"getting data for: {symbol}...")
#         symbol_data = nse_eq(symbol)["preOpenMarket"]
#         full_data[symbol] = symbol_data
#     except Exception as e:
#         print(f"Error fetching data for {symbol}: {e}")
#
# full_data = pd.DataFrame(full_data).transpose()
# full_data.to_csv("pre_market_extract/full_data.csv")
