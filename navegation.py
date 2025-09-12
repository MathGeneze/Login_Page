import streamlit as st

pg = st.navigation([
    
    # Página de login
    st.Page('pages/login.py', title='Login', url_path='Login do Usuário', icon=':material/login:'),
    
    
    # Página de criação de conta
    st.Page('pages/registro.py', title='Criando uma conta', url_path='create_account', icon=':material/account_circle:'),
    
    # página de recuperação de senha
    st.Page('pages/password.py', title='Recuperação de senha', url_path='recuperação_de_senha', icon=':material/password:')
])

pg.run()
