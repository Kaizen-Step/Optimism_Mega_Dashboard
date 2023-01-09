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
    elif query == 'Optimism_TX_Intervals':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2ff0740f-5857-44bf-bdeb-ca47378bcca5/data/latest')
    return None


TX_Optimism = get_data('TX_Optimism')
Luna_daily_tx_vol = get_data('Luna Daily Transaction')
Optimism_TX_Intervals = get_data('Optimism_TX_Intervals')

st.subheader('Transaction Charts')
df = TX_Optimism
df2 = Luna_daily_tx_vol
df4 = Optimism_TX_Intervals


tab_Overtime, tab_Averages = st.tabs(['**Over Time**', '**Averages**'])

with tab_Overtime:
    interval = st.radio('**Time Interval**',
                        ['Daily', 'Weekly', 'Monthly'], key='fees_interval', horizontal=True)

    if st.session_state.fees_interval == 'Daily':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["DAY"], y=df4["CUMULATIVE_TRANSACTIONS_DAILY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["DAY"], y=df4["CUMULATIVE_FEE_DAILY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Daily with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["AVG_BLOCK_TIME_DAILY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='Block Time daily')
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

     # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TPS_DAILY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Daily ')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Weekly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["WEEK"], y=df4["CUMULATIVE_BLOCK_WEEKLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["WEEK"], y=df4["CUMULATIVE_FEE_WEEKLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Weekly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["AVG_BLOCK_TIME_WEEKLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME WEEKLY'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["WEEK"], y=df4["TPS_WEEKLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Weekly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    elif st.session_state.fees_interval == 'Monthly':

        # Total Transaction over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                             name='Total Transaction'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["MONTH"], y=df4["CUMULATIVE_TRANSACTIONS_MONTHLY"],
                              name='CUMULATIVE Transactions'), secondary_y=True)
        fig.update_layout(
            title_text='Total Transactions Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Transaction', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Total Fees over Time with Cumulative Value
        fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TOTAL_FEES_OVER_TIME"],
                             name='Total Fee'), secondary_y=False)
        fig.add_trace(go.Line(x=df4["MONTH"], y=df4["CUMULATIVE_BLOCK_MONTHLY"],
                              name='CUMULATIVE Fee'), secondary_y=True)
        fig.update_layout(
            title_text='Total Fees Monthly with Cumulative Value')
        fig.update_yaxes(
            title_text='Total Fee', secondary_y=False)
        fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # Block Time over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["AVG_BLOCK_TIME_MONTHLY"],
                             name='Average Block Time'), secondary_y=False)
        fig.update_layout(title_text='AVG BLOCK TIME Monthly'.title())
        fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

        # TPs over Time
        fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
        fig.add_trace(go.Bar(x=df4["MONTH"], y=df4["TPS_MONTHLY"],
                             name='TPS'), secondary_y=False)
        fig.update_layout(title_text='TPS Monthly')
        fig.update_yaxes(title_text='TPS', secondary_y=False)
        st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


with tab_Averages:

    # Average Block Time Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df['AVG_BLOCK_TIME'],
                         name='Average Block Time'), secondary_y=False)
    fig.update_layout(title_text='Average Block Time Per Week')
    fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average Transaction Fee Per Transaction Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TRANSACTION_FEE_WEEKLY"],
                         name="AVG TRANSACTION FEE WEEKLY".title()), secondary_y=False)
    fig.update_layout(
        title_text='Average Transaction Fee Per Transaction Per Week')
    fig.update_yaxes(title_text='AVG TRANSACTION FEE WEEKLY',
                     secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average TPS Per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["AVG_TPS"],
                         name="AVG TPS".title()), secondary_y=False)
    fig.update_layout(
        title_text='Average TPS Per Week')
    fig.update_yaxes(title_text='AVG TPS'.title(), secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Weekly Blocks
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df['WEEK'], y=df["TOTAL_BLOCK_WEEKLY"],
                         name="TOTAL BLOCK WEEKLY".title()), secondary_y=False)
    fig.update_layout(title_text='Weekly Blocks')
    fig.update_yaxes(title_text='TOTAL BLOCK WEEKLY', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Average Transactions Fee per Week
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df["WEEK"], y=df["AVG_TRANSACTION_FEE_WEEKLY"],
                         name='Average Transaction Fee'), secondary_y=False)
    fig.update_layout(title_text='Average Transactions Fee per Week')
    fig.update_yaxes(title_text='Average Transaction Fee', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
