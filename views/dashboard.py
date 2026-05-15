import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.title("Générateur")
    
    col1, col2 = st.columns([1, 1.5], gap="large")
    
    with col1:
        st.subheader("Paramètres")
        with st.expander("Identité de marque", expanded=True):
            biz = st.text_input("Nom de l'entreprise", placeholder="ex: Ghost Agency")
            industry = st.selectbox("Secteur d'activité", ["Technologie", "Immobilier", "Luxe", "Santé", "Sport"])
        
        with st.expander("Objectif du post"):
            goal = st.select_slider("Ton", options=["Informatif", "Vendeur", "Viral"])
            
        if st.button("Générer le contenu", type="primary", use_container_width=True):
            if biz:
                with st.spinner("Analyse des données..."):
                    st.session_state.result = generate_social_bundle(biz, industry, goal)
            else:
                st.error("Veuillez entrer un nom d'entreprise.")

    with col2:
        st.subheader("Résultat")
        if "result" in st.session_state:
            st.info("Contenu optimisé")
            st.markdown(st.session_state.result)
            st.button("Copier le texte")
        else:
            st.info("Le contenu généré apparaîtra ici.")
