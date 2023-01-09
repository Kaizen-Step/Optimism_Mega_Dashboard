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
st.set_page_config(page_title='Overview - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Overview')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Data Sources


@st.cache()
def get_data(query):
    if query == 'Overview_Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f7b9a55f-902b-4ed2-b493-d8b95bae4176/data/latest')
    elif query == 'Overview_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e23a6081-e7bc-43b8-977c-f24047794527/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')
    elif query == 'Overview_Total_Staking_Reward':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/97a71654-c83b-4f34-be2c-6f9f826822fd/data/latest')
    elif query == 'Overview_bridge_out':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/89ff4f7f-817e-4337-bff0-b54e4b83b763/data/latest')
    elif query == 'Overview_Supply':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5003e34f-5634-4d36-95e0-bc06bf180327/data/latest')
    elif query == 'Overview_NFT':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/293e5952-c5a5-40b7-a286-d56acef4d9d3/data/latest')
    elif query == 'Overview_HeatmapTX2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cadf8686-2873-4a46-9fd4-2b406d3ae2d6/data/latest')
    elif query == 'Overview_NEARheatmap2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/119a1f32-294a-4749-9d0b-746120829567/data/latest')
    return None


Overview_Optimism = get_data('Overview_Optimism')
Overview_contracts = get_data('Overview_contracts')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')
Overview_Total_Staking_Reward = get_data('Overview_Total_Staking_Reward')
Overview_bridge_out = get_data('Overview_bridge_out')
Overview_Supply = get_data('Overview_Supply')
Overview_NFT = get_data('Overview_NFT')
Overview_HeatmapTX2 = get_data('Overview_HeatmapTX2')
Overview_NEARheatmap2 = get_data('Overview_NEARheatmap2')

# Single Number Overview
st.subheader('Glance')

df1 = Overview_Optimism
df2 = Overview_contracts
df3 = Overview_Contract_Deployed
df4 = Overview_Total_Staking_Reward
df5 = Overview_bridge_out
df6 = Overview_Supply
df7 = Overview_NFT
df9 = Overview_HeatmapTX2
df10 = Overview_NEARheatmap2


c1, c2, c3 = st.columns(3)
with c1:
    st.metric(label='**Transactions Sucsess Rate**',
              value=str(df1["SUCCESS_RATE"].map('{:,.2f}'.format).values[0]))
    st.metric(label='**Avg Fee per Block**',
              value=df1["AVG_FEE_PER_BLOCK"].map('{:,.4f}'.format).values[0])
    st.metric(label='**Total Blocks**',
              value=df1["TOTAL_BLOCKS"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Circulating Supply**',
              value=df6["Circulating Supply"].map('{:,.0f}'.format).values[0])
    st.metric(label='**NFT Sales USD Volume**',
              value=df7["USD Volume"].map('{:,.0f}'.format).values[0])
with c2:
    st.metric(label='**AVG FEE [ETH]**',
              value=str(df1["AVG_FEE"].map('{:,.04}'.format).values[0]))
    st.metric(label='**MAX FEE [ETH]**',
              value=df1["MAX_FEE"].map('{:,.04}'.format).values[0])
    st.metric(label='**TOTAL FEES [ETH]**',
              value=df1["TOTAL_FEES"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Supply**',
              value=df6["Total Supply"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Number of NFT Sellers**',
              value=df7["Number of Sellers"].map('{:,.0f}'.format).values[0])
with c3:
    st.metric(label='**TOTAL TRANSACTIONS**',
              value=str(df1["TOTAL_TRANSACTIONS"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Unique User**',
              value=df1["Total Unique User"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total Contract Deployed**',
              value=df2["Total Contracts Deployed"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Percentage of Circulating Supply**',
              value=df6["Percentage of Circulating Supply"].map('{:,.2f}'.format).values[0])
    st.metric(label='**Number of NFT Buyers**',
              value=df7["Number of Buyers"].map('{:,.0f}'.format).values[0])

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('HeatMaps')


fig = px.density_heatmap(df9, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Failed transactions per minute on hour of day (UTC)",
                         histfunc='avg', title='Failed transactions per minute on hour of day (UTC)', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Failed transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Success transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df9, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="Success transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="Success transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="Success transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Block per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="block per minute on hour of day (UTC)",
                         histfunc='avg', title="Block per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="block per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# User per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                         histfunc='avg', title="User per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# transactions per minute on hour of day (UTC)
fig = px.density_heatmap(df10, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                         histfunc='avg', title="transactions per minute on hour of day (UTC)".title(), nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                  'dtick': 1}, coloraxis_colorbar=dict(title="transactions per minute on hour of day (UTC)"))
fig.update_yaxes(categoryorder='array', categoryarray=week_days)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
