import streamlit as st
def show():
    st.title("GhostContent AI 👻")
    st.write("Générez votre contenu en un clic.")
    if st.button("Se connecter (Démo)"):
        st.session_state.user = True
        st.rerun()
