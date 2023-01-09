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
st.set_page_config(page_title='Wallets - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Opti_newusers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c5020d3e-5e75-499e-8309-5dd7c9bf3998/data/latest')
    elif query == 'Disturbution_Balance':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/defa6d5a-725e-4609-91f4-9c3b313a9df1/data/latest')
    return None


Opti_newusers = get_data('Opti_newusers')
Disturbution_Balance = get_data('Disturbution_Balance')

st.subheader('Wallet Charts')
df = Opti_newusers
df2 = Disturbution_Balance

# Total Number of Active Wallets Per Week + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["WEEKLY"], y=df["ACTIVE_USER"],
                     name="ACTIVE USER"), secondary_y=False)
fig.add_trace(go.Line(x=df["WEEKLY"], y=df["CUMULATIVE_ACTIVE_WALLET"],
                      name="BUY COUNT".title()), secondary_y=True)
fig.update_layout(
    title_text='Total Number of Active Wallets Per Week + Cumulative Number')
fig.update_yaxes(
    title_text="ACTIVE USER", secondary_y=False)
fig.update_yaxes(
    title_text="CUMULATIVE_ACTIVE_WALLET".title(), secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of New Wallets Per Week + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["WEEKLY"], y=df["New Users"],
                     name="New Users"), secondary_y=False)
fig.add_trace(go.Line(x=df["WEEKLY"], y=df["CUMULATIVE_NEW_WALLET"],
                      name="CUMULATIVE_NEW_WALLET".title()), secondary_y=True)
fig.update_layout(
    title_text='Total Number of New Wallets Per Week With Cumulative Value')
fig.update_yaxes(
    title_text="New Users", secondary_y=False)
fig.update_yaxes(
    title_text="CUMULATIVE_NEW_WALLET".title(), secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Disturbution of OP Balance
fig = px.bar(df2, x="BALANCE_RANGE", y="WALLET_NUMBER",
             color="BALANCE_RANGE", title='Disturbution of OP Balance')
fig.update_layout(showlegend=True, xaxis_title="BALANCE_RANGE".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
