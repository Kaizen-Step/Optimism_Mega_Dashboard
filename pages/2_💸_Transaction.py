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
st.set_page_config(page_title='Transactions - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'TX_Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/dff022db-c36b-45d2-b7e8-04c9d5276803/data/latest')
    elif query == 'Luna Daily Transaction':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b08821ca-c8fb-4db0-b95f-4dd0d25df9b9/data/latest')
    return None


TX_Optimism = get_data('TX_Optimism')
Luna_daily_tx_vol = get_data('Luna Daily Transaction')

st.subheader('Transaction Charts')
df = TX_Optimism
df2 = Luna_daily_tx_vol


# Total Transaction Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["TOTAL_TRANSACTIONS_WEEKLY"],
                     name="TOTAL TRANSACTIONS WEEKLY".title()), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df["CUMULATIVE_TRANSACTIONS"],
                      name="CUMULATIVE TRANSACTIONS".title()), secondary_y=True)
fig.update_layout(
    title_text='Total Transaction Per Week With Cumulative Value'.title())
fig.update_yaxes(
    title_text="TOTAL TRANSACTIONS WEEKLY".title(), secondary_y=False)
fig.update_yaxes(title_text="CUMULATIVE TRANSACTIONS".title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Block Time Per Week
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['AVG_BLOCK_TIME'],
              name='Average Block Time'), secondary_y=False)
fig.update_layout(title_text='Average Block Time Per Week')
fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Transaction Fees Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["TOTAL_FEES_WEEKLY"],
                     name="TOTAL FEES WEEKLY".title()), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df["CUMULATIVE_FEE"],
                      name="CUMULATIVE FEE".title()), secondary_y=True)
fig.update_layout(
    title_text='Total Transaction Fees Per Week With Cumulative Value'.title())
fig.update_yaxes(
    title_text="TOTAL FEES WEEKLY".title(), secondary_y=False)
fig.update_yaxes(title_text="CUMULATIVE FEE".title(),
                 secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Blocks
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["TOTAL_BLOCK_WEEKLY"],
              name="TOTAL BLOCK WEEKLY".title()), secondary_y=False)
fig.update_layout(title_text='Weekly Blocks')
fig.update_yaxes(title_text='TOTAL BLOCK WEEKLY', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Transaction Fee Per Transaction Per Week
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TRANSACTION_FEE_WEEKLY"],
              name="AVG TRANSACTION FEE WEEKLY".title()), secondary_y=False)
fig.update_layout(
    title_text='Average Transaction Fee Per Transaction Per Week')
fig.update_yaxes(title_text='AVG TRANSACTION FEE WEEKLY', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average TPS Per Week
fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TPS"],
              name="AVG TPS".title()), secondary_y=False)
fig.update_layout(
    title_text='Average TPS Per Week')
fig.update_yaxes(title_text='AVG TPS'.title(), secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
