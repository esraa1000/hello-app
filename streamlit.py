import streamlit as st
from chatbot import get_financial_advice
from sentiment import get_sentiment_score
from portfolio import PortfolioTracker

# Initialize session state
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# Sidebar: User onboarding
with st.sidebar:
    st.header("User Profile")
    age = st.number_input("Age", min_value=18, max_value=100)
    risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
    # ... other inputs

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["Chatbot", "Sentiment", "Portfolio", "Recommendations"])

# Chatbot Tab
with tab1:
    user_query = st.text_input("Ask a financial question:")
    if user_query:
        response = get_financial_advice(user_query, st.session_state.user_data)
        st.write(response)

# Sentiment Tab
with tab2:
    ticker = st.text_input("Enter stock/crypto symbol:")
    if ticker:
        score = get_sentiment_score(ticker)
        st.plotly_chart(plot_sentiment(score))

# Portfolio Tab
with tab3:
    tracker = PortfolioTracker()
    tracker.display_portfolio()
