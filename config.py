import os

# API Keys and Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")  # Get from environment variable or use default

# Watchlist Settings
DEFAULT_WATCHLIST = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]

# Historical Analysis Settings
HISTORICAL_DAYS = 30  # Number of days to analyze for historical trends 