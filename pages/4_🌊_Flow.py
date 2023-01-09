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
st.set_page_config(page_title='Bridge - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌊 Flow In & Out')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Inflow_OVERALL':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/92bd35cf-043c-41c5-8f44-13beab2b4714/data/latest')
    elif query == 'OPTi_weekly_inflow':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7c27526c-a6b5-4291-ad7e-87c2351afb63/data/latest')
    elif query == 'Outflow_OVERALL':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e615fdbf-4693-41fc-a6a3-1bfe2dfb82be/data/latest')
    elif query == 'daily_bridge_detail':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3b5c115f-5335-4233-b6a8-9bd9ffec9226/data/latest')
    return None


Inflow_OVERALL = get_data('Inflow_OVERALL')
OPTi_weekly_inflow = get_data('OPTi_weekly_inflow')
Outflow_OVERALL = get_data('Outflow_OVERALL')
daily_bridge_detail = get_data('daily_bridge_detail')

st.subheader('InFlow Metrics')

df = Inflow_OVERALL
df2 = OPTi_weekly_inflow
df3 = Outflow_OVERALL
df4 = daily_bridge_detail

# Compare hop VS native bridge
fig = px.bar(df, x="BRIDGE", y="Total Amount Bridged",
             color="Token Bridged", title='Compare hop VS native bridge')
fig.update_layout(showlegend=True, xaxis_title="Total Amount Bridged".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare Inflow tokens Volume
fig = px.pie(df, values="Total Amount Bridged",
             names="Token Bridged", title='Compare Inflow tokens Volume')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare hop VS native bridge- USD Scale
fig = px.bar(df, x="BRIDGE", y="Total Amount Bridged (USD Scale)",
             color="Token Bridged", title='Compare hop VS native bridge')
fig.update_layout(showlegend=True, xaxis_title="Total Amount Bridged (USD Scale)".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare Inflow tokens Volume-USD Scale
fig = px.pie(df, values="Total Amount Bridged (USD Scale)",
             names="Token Bridged", title='Compare Inflow tokens Volume-USD Scale')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Inflow-Compare users
fig = px.bar(df, x="Token Bridged", y="Total Number of Unique Wallets",
             color="BRIDGE", title='Inflow-Compare users')
fig.update_layout(showlegend=True, xaxis_title="Total Number of Unique Wallets".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('OutFlow Metrics')

# Compare Outflow tokens-USD Scale
fig = px.pie(df3, values="Total Amount Bridged (USD Scale)",
             names="Token Bridged", title='Compare Outflow tokens-USD Scale')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare Outflow tokens Volume
fig = px.pie(df3, values="Total Amount Bridged",
             names="Token Bridged", title='Compare Outflow tokens Volume')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare hop VS native bridge volume-USD Scale
fig = px.bar(df3, x="BRIDGE", y="Total Amount Bridged (USD Scale)",
             color="Token Bridged", title='Compare hop VS native bridge volume-USD Scale')
fig.update_layout(showlegend=True, xaxis_title="Total Amount Bridged (USD Scale)".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Compare hop VS native bridge volume
fig = px.bar(df3, x="BRIDGE", y="Total Amount Bridged",
             color="Token Bridged", title='Compare hop VS native bridge volume')
fig.update_layout(showlegend=True, xaxis_title="Total Amount Bridged".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Outflow-Compare users
fig = px.bar(df3, x="Token Bridged", y="Total Number of Unique Wallets",
             color="Token Bridged", title='Outflow-Compare users')
fig.update_layout(showlegend=True, xaxis_title="Total Number of Unique Wallets".title(),
                  yaxis_title=None)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
