import streamlit as st

# Fundo animado da página
with open('styles/style_3.css') as fundo:
    st.markdown(f'<style>{fundo.read()}</style>',
        unsafe_allow_html=True)


st.title('Recuperação de senha.')