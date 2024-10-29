import streamlit as st

# Função para exibir a tela inicial de módulos
def tela_modulos():
    st.title("Módulos")
    st.write("Clique em um módulo para ver os relatórios correspondentes.")
    
    # Definindo os módulos
    modulos = ["A", "B", "C", "D", "E", "F"]
    
    # Exibindo os módulos como botões em uma grid
    cols = st.columns(3)
    for i, modulo in enumerate(modulos):
        with cols[i % 3]:
            if st.button(f"Módulo {modulo}"):
                st.session_state.modulo_selecionado = modulo
                st.session_state.tela_atual = "relatorios"

# Função para exibir a tela de relatórios de acordo com o módulo selecionado
def tela_relatorios():
    modulo = st.session_state.modulo_selecionado
    st.title(f"Relatórios do Módulo {modulo}")
    
    # Exibindo o menu de módulos novamente para fácil navegação
    st.write("Selecione outro módulo:")
    cols = st.columns(6)
    modulos = ["A", "B", "C", "D", "E", "F"]
    for i, m in enumerate(modulos):
        with cols[i]:
            if st.button(f"{m}", key=f"modulo_{m}"):
                st.session_state.modulo_selecionado = m
                modulo = m  # Atualiza o módulo selecionado

    # Submódulos ou relatórios associados ao módulo selecionado
    relatorios = {
        "A": ["Relatório A", "Relatório B", "Relatório C", "Relatório D"],
        "B": ["Relatório E", "Relatório F", "Relatório G", "Relatório H"],
        "C": ["Relatório I", "Relatório J", "Relatório K", "Relatório L"],
        "D": ["Relatório M", "Relatório N", "Relatório O", "Relatório P"],
        "E": ["Relatório Q", "Relatório R", "Relatório S", "Relatório T"],
        "F": ["Relatório U", "Relatório V", "Relatório W", "Relatório X"]
    }
    
    # Exibindo os relatórios do módulo selecionado
    st.write("Relatórios:")
    for relatorio in relatorios[modulo]:
        st.write(relatorio)

    # Botão para voltar à tela inicial
    if st.button("Voltar aos Módulos"):
        st.session_state.tela_atual = "modulos"

# Inicializando a sessão e a tela inicial
if "tela_atual" not in st.session_state:
    st.session_state.tela_atual = "modulos"
if "modulo_selecionado" not in st.session_state:
    st.session_state.modulo_selecionado = None

# Controlando qual tela exibir
if st.session_state.tela_atual == "modulos":
    tela_modulos()
elif st.session_state.tela_atual == "relatorios":
    tela_relatorios()
