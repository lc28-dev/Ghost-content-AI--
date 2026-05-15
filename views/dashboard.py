import streamlit as st
def show():
    st.title("🚀 Dashboard")
    st.write("Bienvenue dans votre espace de création.")
    if st.button("Déconnexion"):
        st.session_state.user = None
        st.rerun()
