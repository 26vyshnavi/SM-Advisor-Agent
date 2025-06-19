from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import yfinance as yf
from datetime import datetime
from config import OPENAI_API_KEY
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Initialize the LLM with proper configuration
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=OPENAI_API_KEY
)

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    today_data = stock.history(period="1d")
    if today_data.empty:
        raise ValueError(f"No data found for symbol {symbol}")
    
    latest_data = today_data.iloc[-1]
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "open": latest_data["Open"],
        "high": latest_data["High"],
        "low": latest_data["Low"],
        "close": latest_data["Close"],
        "volume": latest_data["Volume"]
    }

def summarize_stock(data, symbol):
    prompt = ChatPromptTemplate.from_template("""
    Summarize today's market data for {symbol}:
    Date: {date}
    Opening Price: {open}
    High Price: {high}
    Low Price: {low}
    Closing Price: {close}
    Volume: {volume}

    Provide a brief summary including market trends and possible insights.
    """)
    
    chain = prompt | llm
    summary = chain.invoke({"symbol": symbol, **data}).content
    return summary

# Example usage:
stock_data = fetch_stock_data("AAPL")
print(summarize_stock(stock_data, "AAPL"))

