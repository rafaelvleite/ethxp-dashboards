import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('LOGO ETH - PERFIL V2.png'))

st.header('ETHXP Dashboards')

st.subheader('Relevant dashboards for better insights')

icon_size = 20

st_button('', 'https://rafaelvleite-options-volatility-options-streamlit-oubv79.streamlit.app/?embedded=true', 'Volatilidade das Opções de ETH', icon_size)
st_button('', 'https://rafaelvleite-ichimoku-backtest-stream-ichimoku-streamlit-i2cjli.streamlit.app/?embedded=true', 'Backtests de Ichimoku', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashes-eth-dashboard-24hs-gekdez.streamlit.app/?embedded=true', 'Deribit ETH Options 24 Hours', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashes-eth-dashboard-48hs-wwwsl7.streamlit.app/?embedded=true', 'Deribit ETH Options 48 Hours', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashes-eth-dashboard-weekly-2cts9h.streamlit.app/?embedded=true', 'Deribit ETH Options Weekly', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashe-eth-dashboard-monthly-6yspoz.streamlit.app/?embedded=true', 'Deribit ETH Options Monthly', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-das-eth-dashboard-quarterly-x6yxsl.streamlit.app/?embedded=true', 'Deribit ETH Options Quarterly', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-da-eth-dashboard-semesterly-5pg2ys.streamlit.app/?embedded=true', 'Deribit ETH Options Semesterly', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashe-eth-dashboard-anually-ty19hf.streamlit.app/?embedded=true', 'Deribit ETH Options Anually', icon_size)

