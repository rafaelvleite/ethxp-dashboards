import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('LOGO ETH - PERFIL V2.png'))

st.header('ETHXP Dashboards')

st.subheader('Relevant dashboards for better insights')

icon_size = 20

st_button('', 'https://rafaelvleite-ethxp-streamlit-dashes-eth-dashboard-24hs-gekdez.streamlit.app/', 'Deribit ETH Options 24 Hours', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashes-eth-dashboard-48hs-wwwsl7.streamlit.app/', 'Deribit ETH Options 48 Hours', icon_size)
#st_button('', 'https://data-professor.medium.com/', 'Deribit Historic Data for ETH Options: Friday Contracts', icon_size)
st_button('', 'https://rafaelvleite-ethxp-streamlit-dashe-eth-dashboard-monthly-6yspoz.streamlit.app/', 'Deribit ETH Options Monthly', icon_size)
#st_button('', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Deribit Historic Data for ETH Options: Quarterly Contracts', icon_size)
#st_button('', 'https://sendfox.com/dataprofessor/', 'Deribit Historic Data for ETH Options: Semesterly Contracts', icon_size)

