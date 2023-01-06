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
st.set_page_config(page_title='Development - Terra Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Developments')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'weekly_active_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/33bd8b25-d005-4ee6-a036-fba16f422778/data/latest')
    elif query == 'new_deploy_contract':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8e86949f-ebe0-4852-9f24-455d2f8b9c16/data/latest')
    elif query == 'Most_popular_contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c7115145-d91f-4979-b648-0c003446682a/data/latest')
    return None


weekly_active_contracts = get_data('weekly_active_contracts')
new_deploy_contract = get_data('new_deploy_contract')
Most_popular_contracts = get_data('Most_popular_contracts')

st.subheader('Development Charts')
df = weekly_active_contracts
df2 = new_deploy_contract
df3 = Most_popular_contracts

# Weekly active contracts
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df['DATE'], y=df["Active contract"],
                     name='Number of Active Contracts'), secondary_y=False)
fig.update_layout(
    title_text='Weekly active contracts')
fig.update_yaxes(
    title_text='Number of Active Contracts', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# New Deployed Contracts
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2['DATE'], y=df2["New Contract"],
                     name="New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["Cum New Contract"],
                      name="Cum New Contract"), secondary_y=True)
fig.update_layout(
    title_text='New Deployed Contracts')
fig.update_yaxes(
    title_text="New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Most_popular_contracts
fig = px.pie(df3, values="Number of TX", names="Contract Name",
             title='Most_popular_contracts')
fig.update_layout(legend_title='"Contract Name"', legend_y=0.5)
fig.update_traces(textinfo='percent+label', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
