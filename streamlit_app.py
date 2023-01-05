import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''
    
col1, col2, col3 = st.columns(3)
col2.image(Image.open('LOGO ETH - PERFIL V2.png'))

st.header('ETHXP Dashboards')

st.info(mystyle, 'Relevant dashboards for better insights')

icon_size = 20

st_button('', 'https://youtube.com/dataprofessor', 'Deribit Historic Data for ETH Options: 24 Hours Contracts', icon_size)
st_button('', 'https://youtube.com/codingprofessor', 'Deribit Historic Data for ETH Options: 48 Hours Contracts', icon_size)
st_button('', 'https://data-professor.medium.com/', 'Deribit Historic Data for ETH Options: Friday Contracts', icon_size)
st_button('', 'https://twitter.com/thedataprof/', 'Deribit Historic Data for ETH Options: Monthly Contracts', icon_size)
st_button('', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Deribit Historic Data for ETH Options: Quarterly Contracts', icon_size)
st_button('', 'https://sendfox.com/dataprofessor/', 'Deribit Historic Data for ETH Options: Semesterly Contracts', icon_size)

