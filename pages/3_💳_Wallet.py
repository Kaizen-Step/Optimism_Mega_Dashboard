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
st.set_page_config(page_title='Wallets - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'New_and_Active_Wallets':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e9e0c78c-0d63-44a8-aab1-4dcc5216891b/data/latest')
    return None


New_and_Active_Wallets = get_data('New_and_Active_Wallets')

st.subheader('Wallet Charts')
df = New_and_Active_Wallets

# Total Number of Active Wallets Per Week With Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['ACTIVE_WALLETS'],
                     name='Number of ACTIVE WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_ACTIVE_WALLET'],
                      name='CUMULATIVE ACTIVE WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of Active Wallets Per Week With Cumulative Value')
fig.update_yaxes(
    title_text='Number of ACTIVE WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Number of New Wallets Per Week With Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['WEEK'], y=df['NEW_WALLETS'],
                     name='NEW WALLETS'), secondary_y=False)
fig.add_trace(go.Line(x=df['WEEK'], y=df['CUMULATIVE_NEW_WALLET'],
                      name='CUMULATIVE NEW WALLET'), secondary_y=True)
fig.update_layout(
    title_text='Total Number of New Wallets Per Week With Cumulative Number')
fig.update_yaxes(
    title_text='Number of NEW WALLETS', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Number', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
