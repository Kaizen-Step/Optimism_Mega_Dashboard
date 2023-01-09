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
st.set_page_config(page_title='Development - Optimism Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Developments')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'weekly_active_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9fb60984-58e2-413b-a455-fb5c53a266ba/data/latest')
    elif query == 'weekly_new_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a8c68656-05c0-45d4-a64e-3e8378d3edae/data/latest')
    elif query == 'Most_popular_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/30e1a706-3d9a-401c-b508-90f5a265ffaa/data/latest')
    elif query == 'Top_Contracts_TXfee':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5e7e57fe-08d8-431e-a6f9-0c9f2732d125/data/latest')
    return None


weekly_active_contracts = get_data('weekly_active_contracts')
weekly_new_contracts = get_data('weekly_new_contracts')
Most_popular_contracts = get_data('Most_popular_contracts')
Top_Contracts_TXfee = get_data('Top_Contracts_TXfee')

st.subheader('Development Charts')
df = weekly_active_contracts
df2 = weekly_new_contracts
df3 = Most_popular_contracts
df4 = Top_Contracts_TXfee

# Weekly active contracts
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['DATE'], y=df["Active contract"],
                     name='Number of Active Contracts'), secondary_y=False)
fig.update_layout(
    title_text='Weekly active contracts')
fig.update_yaxes(
    title_text='Number of Active Contracts', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# New deploy contract + Cumulative Number
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2["New Contract"],
                     name="New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["Cum New Contract"],
                      name="Cum New Contract"), secondary_y=True)
fig.update_layout(
    title_text='New deploy contract With Cumulative Value')
fig.update_yaxes(
    title_text="New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# most popular contracts based on Trancactions
fig = px.pie(df3, values="Number of Transactions", names="PROJECT_NAME",
             title='most popular contracts based on Trancactions'.title())
fig.update_layout(legend_title='Project Name', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# most popular contracts based on Users
fig = px.pie(df3, values="Number of User", names="PROJECT_NAME",
             title='most popular contracts based on Users'.title())
fig.update_layout(legend_title='Project Name', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on User
fig = px.bar(df3.sort_values(["DATE", "Number of User"], ascending=[
             True, False]), x="DATE", y="Number of User", color="PROJECT_NAME", title='Weekly Top Contracts Based on User')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of User")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on Transactions
fig = px.bar(df3.sort_values(["DATE", "Number of Transactions"], ascending=[
             True, False]), x="DATE", y="Number of Transactions", color="PROJECT_NAME", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="Number of Transactions")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# most popular contracts based on Transaction Fee
fig = px.pie(df4, values="TX_FEE", names="PROJECT_NAME",
             title='most popular contracts based on Transaction Fee'.title())
fig.update_layout(legend_title="TX FEE", legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on Transaction Fee
fig = px.bar(df4.sort_values(["DATE", "TX_FEE"], ascending=[
             True, False]), x="DATE", y="TX_FEE", color="PROJECT_NAME", title='Weekly Top Contracts Based on Transaction Fee')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="TX FEE")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
