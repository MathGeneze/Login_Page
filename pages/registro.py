import streamlit as st

# Fundo animado da página
with open('styles/style_2.css') as fundo:
    st.markdown(f'<style>{fundo.read()}</style>',
        unsafe_allow_html=True)


st.title('Cadastro de clientes')

nome = st.text_input('Nome', placeholder='João da Silva')
email = st.text_input('Email', placeholder='joão.silva@gmail.com')
senha = st.text_input('Senha', placeholder='123456789', type='password')
telefone = st.text_input('Telefone', placeholder='55 12345 6789')
