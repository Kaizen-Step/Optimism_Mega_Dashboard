# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Optimism MegaDashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('Optimism Dashboard')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/optimism-logo.png'))

with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""  # Optimism (blockchain) #   """)
st.write(""" Optimism is a Layer 2 scaling solution for Ethereum that can support all of Ethereum's Dapps. Instead of running all computation and data on the Ethereum network, Optimism puts all transaction data on-chain and runs computation off-chain, increasing Ethereum's transactions per second and decreasing transaction fees.  
Optimism is a layer 2 chain, meaning it functions on top of Ethereum mainnet (layer 1). Transactions take place on Optimism, but the data about transactions get posted to mainnet where they are validated. It’s like driving in a less crowded side street while benefiting from the security of a highway.
Optimism is the second-largest Ethereum layer 2 with a total of 313 million locked into its smart contracts, as of this writing, according to Defi Llama. Arbitrum comes first with 1.32 billion.
Synthetix, a derivatives liquidity protocol, is the largest protocol on Optimism, with a total value locked (TVL) of 125 million. Uniswap, a decentralized exchange (DEX), is the second most popular protocol on the chain. As of this writing, there are 35 protocols on Optimism with at least 1,000 locked into their smart contracts.

""")
st.write("""   
##### Sources #####   """)
st.write("""    1.https: // www.scoutinsights.co. in /post/luna-and -lunc-coins-destroyed  
        2.https: // www.bloomberg.com/news/articles/2022-05-14  
        3.https: // social.techcrunch.com/2022/05/12/  
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
