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
st.set_page_config(page_title='NFT - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🎴NFT')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NFT_Opt':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d1604b01-09f8-4973-944d-f53f0dc65268/data/latest')
    elif query == 'weekly_new_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a8c68656-05c0-45d4-a64e-3e8378d3edae/data/latest')
    elif query == 'Most_popular_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/30e1a706-3d9a-401c-b508-90f5a265ffaa/data/latest')
    elif query == 'Top_Contracts_TXfee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5e7e57fe-08d8-431e-a6f9-0c9f2732d125/data/latest')
    elif query == 'Average_SalesVolume_DaysWeek':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/815f4b33-96ea-4464-9371-0bb41069a627/data/latest')
    elif query == 'Buying_Selling_NFT':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7b4f21b8-4ac6-4103-ac0b-10d1dbd47b01/data/latest')
    elif query == 'NFTs_held_Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/125c20d5-3349-48d0-a80f-4921f8e9f27e/data/latest')
    elif query == 'Weekly_New_Holders':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eee94e71-1ce3-47a0-b951-6661925d84e7/data/latest')
    elif query == 'OPTI_Top_Buyers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3c30b33e-207e-4304-a007-105cbd255bc1/data/latest')
    elif query == 'MostPopular_NFT_Collections':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/727639a2-0e15-45cb-86ca-d8b1b6b15364/data/latest')
    elif query == 'Top10_Highest_NFT':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c4dce890-bb33-4049-96d5-245964c3630c/data/latest')
    return None


NFT_Opt = get_data('NFT_Opt')
weekly_new_contracts = get_data('weekly_new_contracts')
Most_popular_contracts = get_data('Most_popular_contracts')
Top_Contracts_TXfee = get_data('Top_Contracts_TXfee')
Average_SalesVolume_DaysWeek = get_data('Average_SalesVolume_DaysWeek')
Buying_Selling_NFT = get_data('Buying_Selling_NFT')
NFTs_held_Users = get_data('NFTs_held_Users')
Weekly_New_Holders = get_data('Weekly_New_Holders')
OPTI_Top_Buyers = get_data('OPTI_Top_Buyers')
MostPopular_NFT_Collections = get_data('MostPopular_NFT_Collections')
Top10_Highest_NFT = get_data('Top10_Highest_NFT')

st.subheader('NFT Metrics')

df = NFT_Opt
df2 = weekly_new_contracts
df3 = Most_popular_contracts
df4 = Top_Contracts_TXfee
df5 = Average_SalesVolume_DaysWeek
df6 = Buying_Selling_NFT
df7 = NFTs_held_Users
df8 = Weekly_New_Holders
df9 = OPTI_Top_Buyers
df10 = MostPopular_NFT_Collections
df11 = Top10_Highest_NFT


# Weekly Sales ➡ Left Axis: Number of Sales | Right Axis: Cumulative Number of Sales
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["Date"], y=df["Number of Sales"],
                     name="Number of Sales"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Cumulative - Number of Sales"],
                      name="Cumulative - Number of Sales"), secondary_y=True)
fig.update_layout(
    title_text='Weekly Sales with Cumulative Value')
fig.update_yaxes(
    title_text="Number of Sales", secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Sales', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Buyers ➡ Left Axis: Number of Sales | Right Axis: Cumulative Number of Sales
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["Date"], y=df["Number of Buyers"],
                     name="Number of Buyers"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Cumulative - Number of Buyers"],
                      name="Cumulative - Number of Buyers"), secondary_y=True)
fig.update_layout(
    title_text='Weekly Buyers with Cumulative Value')
fig.update_yaxes(
    title_text="Number of Buyers", secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE BUYERS', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Sellers➡ Left Axis: Number of Sellers| Right Axis: Cumulative Number of Sellers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["Date"], y=df["Number of Sellers"],
                     name="Number of Sellers"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Cumulative - Number of Sellers"],
                      name="Cumulative - Number of Sellers"), secondary_y=True)
fig.update_layout(
    title_text='Weekly Sellers with Cumulative Value')
fig.update_yaxes(
    title_text="Number of Sellers", secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Sellers', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Sales USD Volume➡ Left Axis: Number of Sellers| Right Axis: Cumulative Number of Sellers
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["Date"], y=df["USD Volume"],
                     name="USD Volume"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Cumulative - USD Volume"],
                      name="Cumulative - USD Volume"), secondary_y=True)
fig.update_layout(
    title_text='Weekly Sales USD Volume with Cumulative Value')
fig.update_yaxes(
    title_text="USD Volume", secondary_y=False)
fig.update_yaxes(title_text="Cumulative - USD Volume", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Values➡   USD per Sele | USD per Buyer |  USD per Seller
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["Date"], y=df["Average USD per Sale"],
                      name="Average USD per Sale"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Average USD per Buyer"],
                      name="Average USD per Buyer"), secondary_y=False)
fig.add_trace(go.Line(x=df["Date"], y=df["Average USD per Seller"],
                      name="Average USD per Seller"), secondary_y=False)
fig.update_layout(title_text='"Average USD Values"')
fig.update_yaxes(title_text='USD', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Average Sales Volume by Days of the Week
fig = px.pie(df5, values="AVG_VOLUME",
             names="WEEK_DAY", title='Average Sales Volume by Days of the Week')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# OPTI-Distribution of Average Number of Days Between Buying and Selling an NFT
fig = px.pie(df6, values="TOTAL",
             names="TYPE", title='OPTI-Distribution of Average Number of Days Between Buying and Selling an NFT')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Distribution of the number of NFTs held by Users
fig = px.pie(df7, values="TOTAL",
             names="OWNER_TYPE", title='Distribution of the number of NFTs held by Users')
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly New Holders
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df8["WEEK"], y=df8["NEW_HOLDERS"],
                     name="NEW_HOLDERS"), secondary_y=False)
fig.add_trace(go.Line(x=df8["WEEK"], y=df8["CUMU_NEW_HOLDERS"],
                      name="CUMUlative NEW HOLDERS".title()), secondary_y=True)
fig.update_layout(
    title_text='Weekly New Holders')
fig.update_yaxes(
    title_text="NEW_HOLDERS", secondary_y=False)
fig.update_yaxes(title_text="CUMUlative NEW HOLDERS".title(), secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Most Popular NFT Collections
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df10["PROJECT_NAME"], y=df10["VOLUME"],
                     name="VOLUME"), secondary_y=False)
fig.add_trace(go.Line(x=df10["PROJECT_NAME"], y=df10["BUY_COUNT"],
                      name="BUY_COUNT".title()), secondary_y=True)
fig.update_layout(
    title_text='Most Popular NFT Collections')
fig.update_yaxes(
    title_text="VOLUME", secondary_y=False)
fig.update_yaxes(title_text="BUY_COUNT".title(), secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
