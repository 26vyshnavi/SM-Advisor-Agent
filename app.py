import streamlit as st
import pandas as pd
from workflow import stock_advisor
from analysis import generate_technical_report
from config import DEFAULT_WATCHLIST

st.set_page_config(page_title="Stock Market Advisor", page_icon="📈")

st.title("📈 Stock Market Advisor")
st.write("Your AI-powered stock market analysis assistant")

# Sidebar for settings
st.sidebar.header("Settings")

# Watchlist management
st.sidebar.subheader("Watchlist")
watchlist = st.sidebar.multiselect(
    "Select stocks to monitor",
    options=DEFAULT_WATCHLIST,
    default=DEFAULT_WATCHLIST[:3]
)

# Main content
selected_stock = st.selectbox("Select a stock to analyze", watchlist)

if selected_stock:
    # Generate reports
    market_summary = stock_advisor(selected_stock)
    technical_report = generate_technical_report(selected_stock)
    
    # Display reports in tabs
    tab1, tab2 = st.tabs(["Market Summary", "Technical Analysis"])
    
    with tab1:
        st.markdown(market_summary)
    
    with tab2:
        st.markdown(technical_report)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Stock Market Advisor") 