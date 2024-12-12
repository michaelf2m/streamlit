from keycloak import KeycloakOpenID
import streamlit as st

# Configuração do Keycloak
KEYCLOAK_SERVER_URL = "http://localhost:8080/auth/"
KEYCLOAK_REALM = "teste-reports"
KEYCLOAK_CLIENT_ID = "streamlit-app"

# Inicializar Keycloak
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
    verify=True,
)

# Autenticação
def authenticate_user(username, password):
    try:
        token = keycloak_openid.token(username, password)
        return token
    except Exception as e:
        st.error(f"Erro de autenticação: {e}")
        return None

# Interface Streamlit
st.title("Login com Keycloak")

# Formulário de login
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

if st.button("Login"):
    token = authenticate_user(username, password)
    if token:
        st.success("Login realizado com sucesso!")
        user_info = keycloak_openid.userinfo(token["access_token"])
        st.json(user_info)
    else:
        st.error("Falha na autenticação.")
