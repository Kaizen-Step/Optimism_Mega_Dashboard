# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Overview - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Overview')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources


@st.cache()
def get_data(query):
    if query == 'Overview_Supply':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2e9b8bd7-11f8-4856-9e1d-31c34adb5c45/data/latest')
    elif query == 'Overview_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eae94398-3e31-4f57-a188-7832b2fc542c/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')
    elif query == 'Overview_Total_Staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/97a71654-c83b-4f34-be2c-6f9f826822fd/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    return None


Overview_Supply = get_data('Overview_Supply')
Overview_Transactions = get_data('Overview_Transactions')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')

# Single Number Overview
st.subheader('Overview')
df1 = Overview_Supply
df2 = Overview_Transactions
df3 = Overview_Contract_Deployed
df4 = Overview_Total_Staking_Reward
df5 = Overview_bridge_out

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Luna Total Supply**',
              value=str(df1['TOTAL_SUPPLY'].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Luna Circulating Supply**',
              value=df1['CIRCULATING_SUPPLY'].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Contract Deployed**',
              value=df3['Total Contracts Deployed'].map('{:,.0f}'.format).values[0])
with c2:
    st.metric(label='**Transactions Success Rate**',
              value=str(df2["AVERAGE_DAILY_SUCCESS_RATE"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Average Daily Transactions**',
              value=df2["AVERAGE_DAILY_TRANSACTION"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Staking Reward**',
              value=df4["CUMULATIVE_STAKING_REWARDS"].map('{:,.0f}'.format).values[0])
with c3:
    st.metric(label='**Bridge out-Number of Unique Users**',
              value=str(df5["ACTIVE_USERS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Bridge out-Total TX of luna**',
              value=df5["NUMBER"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Bridge out-Total volume of luna**',
              value=df5["VOLUME"].map('{:,.0f}'.format).values[0])
