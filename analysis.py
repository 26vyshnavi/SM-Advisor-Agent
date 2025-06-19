import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from config import HISTORICAL_DAYS

def get_historical_data(symbol, days=HISTORICAL_DAYS):
    """Fetch historical stock data."""
    stock = yf.Ticker(symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    return stock.history(start=start_date, end=end_date)

def calculate_trends(data):
    """Calculate various technical indicators and trends."""
    # Calculate moving averages
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Calculate RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Calculate MACD
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()
    
    return data

def analyze_trends(symbol):
    """Analyze historical trends and generate insights."""
    data = get_historical_data(symbol)
    data = calculate_trends(data)
    
    latest = data.iloc[-1]
    prev = data.iloc[-2]
    
    insights = {
        'price_trend': 'Bullish' if latest['Close'] > latest['SMA_20'] else 'Bearish',
        'rsi_signal': 'Overbought' if latest['RSI'] > 70 else 'Oversold' if latest['RSI'] < 30 else 'Neutral',
        'macd_signal': 'Bullish' if latest['MACD'] > latest['Signal_Line'] else 'Bearish',
        'volatility': data['Close'].pct_change().std() * 100,
        'avg_volume': data['Volume'].mean(),
        'price_change': ((latest['Close'] - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100
    }
    
    return insights

def generate_technical_report(symbol):
    """Generate a comprehensive technical analysis report."""
    insights = analyze_trends(symbol)
    
    report = f"""
Technical Analysis Report for {symbol}:
----------------------------------------
Price Trend: {insights['price_trend']}
RSI Signal: {insights['rsi_signal']}
MACD Signal: {insights['macd_signal']}
Volatility: {insights['volatility']:.2f}%
Average Volume: {insights['avg_volume']:,.0f}
Price Change: {insights['price_change']:.2f}%
"""
    return report 