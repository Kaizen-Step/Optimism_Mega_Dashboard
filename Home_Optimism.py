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
st.write(""" 
Optimism is a layer 2 chain, meaning it functions on top of Ethereum mainnet (layer 1). Transactions take place on Optimism, but the data about transactions get posted to mainnet where they are validated. It’s like driving in a less crowded side street while benefiting from the security of a highway.
Optimism is the second-largest Ethereum layer 2 with a total of 313 million locked into its smart contracts, according to Defi Llama. Arbitrum comes first with 1.32 billion.  
Synthetix, a derivatives liquidity protocol, is the largest protocol on Optimism, with a total value locked (TVL) of 125 million. Uniswap, a decentralized exchange (DEX), is the second most popular protocol on the chain. As of this writing, there are 35 protocols on Optimism with at least 1,000 locked into their smart contracts.



 ### How does Optimism work? ### 
Optimism uses a technology called rollups, specifically Optimistic rollups.
They’re called rollups because they roll up (or bundle) the data about hundreds of transactions – non-fungible token (NFT) mints, token swaps … any transaction! – into a single transaction on Ethereum mainnet (layer 1).When so many transactions are rolled up into a single transaction, the blockchain transaction, or "gas," fee required to pay comes down to only one transaction, conveniently distributed across everyone involved.  
And they’re called Optimistic rollups because transactions are assumed to be valid until they are proven false, or in other words, innocent until proven guilty.  
There’s a time window during which potentially invalid transactions can be challenged by submitting a “fraud proof” and running the transactions’ computations with reference to available state data. Optimism reimburses the gas needed to run the computation of the fraud proof. (Here’s a more technically detailed explanation of the process.)
Optimism launched its OP token on May 31. A total of 231,000 addresses were eligible to claim 214 million OP tokens for free (known as an “airdrop”). That accounts for 5% of the total 4.29 billion supply, meaning 95% of the supply has yet to hit the market.



""")
st.write("""   
##### Sources #####   """)
st.write("""    1.https://www.coindesk.com/learn/what-is-optimism/   
                2.https://thedefiant.io/what-is-optimism 

              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
