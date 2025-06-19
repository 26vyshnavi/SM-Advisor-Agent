# 📈 Stock Market Advisor

An AI-powered stock market analysis application that provides real-time market data, technical analysis, and AI-generated insights for stock market investments.

## 🚀 Features

- **Real-time Stock Data**: Fetch current market data using Yahoo Finance API
- **AI-Powered Analysis**: Generate intelligent market summaries using OpenAI's GPT-3.5
- **Technical Analysis**: Comprehensive technical indicators including RSI, MACD, and moving averages
- **Interactive Web Interface**: Beautiful Streamlit dashboard for easy navigation
- **Customizable Watchlist**: Monitor multiple stocks simultaneously
- **Historical Trend Analysis**: Analyze stock performance over time

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Alpha vantage key 

## 🛠️ Installation

1. **Clone or download the project files**

2. **Navigate to the project directory**:
   ```bash
   cd "SM Advisor Agent"
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your OpenAI API key**:
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Set it as an environment variable:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - Or update it directly in `config.py`

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser**:
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

3. **Using the application**:
   - Select stocks from the watchlist in the sidebar
   - View market summaries and technical analysis
   - Switch between different analysis tabs

## 📁 Project Structure

```
SM Advisor Agent/
├── app.py              # Main Streamlit web interface
├── workflow.py         # Core business logic
├── summarize.py        # Stock data fetching and AI summarization
├── analysis.py         # Technical analysis and indicators
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Configuration

### API Keys
- **OpenAI API Key**: Required for AI-powered market summaries
- Set in `config.py` or as environment variable `OPENAI_API_KEY`

### Customization
- **Watchlist**: Modify `DEFAULT_WATCHLIST` in `config.py`
- **Analysis Period**: Adjust `HISTORICAL_DAYS` in `config.py`

## 📊 Features Explained

### Market Summary
- Current day's trading data
- Opening, closing, high, and low prices
- Trading volume
- AI-generated insights and trends

### Technical Analysis
- **RSI (Relative Strength Index)**: Momentum indicator
- **MACD**: Trend-following momentum indicator
- **Moving Averages**: 20-day and 50-day SMAs
- **Volatility Analysis**: Price volatility over time
- **Volume Analysis**: Average trading volume

## 🛠️ Dependencies

- `streamlit`: Web interface framework
- `yfinance`: Yahoo Finance API for stock data
- `langchain-openai`: OpenAI integration for AI analysis
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computations

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

2. **API Key Errors**:
   - Verify your OpenAI API key is set correctly
   - Check if the API key has sufficient credits

3. **Stock Data Errors**:
   - Ensure internet connection is stable
   - Verify stock symbols are valid

4. **Streamlit Issues**:
   - Run with `streamlit run app.py` (not `python app.py`)
   - Check if port 8501 is available

## 📈 Supported Stocks

The application supports all stocks available on Yahoo Finance, including:
- US stocks (e.g., AAPL, MSFT, GOOGL)
- International stocks
- ETFs and mutual funds

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving documentation
- Adding new technical indicators

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It should not be considered as financial advice. Always do your own research and consult with financial professionals before making investment decisions.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Verify your API keys and internet connection
3. Ensure all dependencies are properly installed

---

**Happy Trading! 📈** 
