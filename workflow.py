from summarize import fetch_stock_data, summarize_stock

def stock_advisor(symbol):
    data = fetch_stock_data(symbol)
    summary = summarize_stock(data, symbol)

    result = f"""
📅 Stock Market Summary for {symbol} ({data['date']})

{summary}
"""
    return result

# Example usage:
print(stock_advisor("MSFT"))

