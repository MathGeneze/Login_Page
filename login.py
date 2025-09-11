# Simulador de uma login page

import streamlit as st

st.markdown(
    """
    <style>    
    .stApp {
        background-image: url('https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzQ0aHlqbjhuZm9hZzEyYm5xb25hcm1hOXc4azd0c3EwdjVmdTR3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/p6EDJOPtyd0DJSuDef/giphy.gif');
        background-size: cover;
        background-repeat: no-repeat;
    }    
    </style> 
    """,
    unsafe_allow_html=True
)

# st.dialog retorna um pop-up 
@st.dialog('Alert')
def login_validation(usr, passw):
    if usr == '' or passw == '':
        st.error('**Please enter your username or password.**')
    else:
        st.success('Login successfull.')

# -- Criando o formulário de login
with st.form('Sign_In'):
    
    st.title('Sign In')
    st.caption('Please enter your user and password.')
    st.divider()
    
    # Nome de Usuário e Senha
    user = st.text_input('User', placeholder='ex: email@gmail.com')
    password = st.text_input('Password', type='password', placeholder='ex: 123456')
    
    # Botão de enviar
    botao_submit = st.form_submit_button('Submit', type='primary', use_container_width=True)
    
    colunas_botao = st.columns(2)
    
    
    # -- Botão de conectar com o Google
    with colunas_botao[0]:
    
        botao_google = st.form_submit_button('Connect with Google', type='secondary', icon=':material/mail:', use_container_width=True,)
        
        
    # -- Botão de conectar com o LinkedIn
    with colunas_botao[1]:
    
        botao_linkedin = st.form_submit_button('Connect with LinkedIn', type='secondary', icon=':material/link:', use_container_width=True)
    
    colunas_extra = st.columns(3)
    
    # -- Checkbox para relembrar os dados do usuário
    with colunas_extra[0]:
        remember_me = st.checkbox('Remember me')
        
    # -- Link para aba Forgot Password
    with colunas_extra[1]:
    
        forgot_password = st.html('<p><a href="https://google.com">Forgot Password</a></p>')
    
    # -- Criando uma conta
    with colunas_extra[2]:
        create_account = st.html('<p><a href="https://google.com">Create an Account</a></p>')
        
    # Se o botão for clicado, a função irá verificar infos vazias
    if botao_submit:
        login_validation(user, password)

