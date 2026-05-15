import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    # CSS pour un look haut de gamme (fond dégradé, cartes vitrées)
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            border: none; color: white; padding: 10px 24px; border-radius: 8px; font-weight: bold;
        }
        .artisan-card {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("⚒️ Assistant GhostContent")
    st.write("Créez du contenu qui valorise votre savoir-faire.")

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown('<div class="artisan-card">', unsafe_allow_html=True)
        biz = st.text_input("Nom de votre entreprise", placeholder="ex: Guillin Maçonnerie")
        
        # Secteurs spécialisés Artisans
        secteurs = [
            "Maçonnerie / Gros Oeuvre", "Menuiserie / Bois", "Plomberie / Chauffage", 
            "Électricité", "Peinture / Décoration", "Paysagiste / Jardin", 
            "Rénovation complète", "Architecture d'intérieur"
        ]
        industry = st.selectbox("Votre métier", secteurs)
        
        # Objectifs sérieux
        objectifs = {
            "Visibilité (Se faire connaître)": "gagner en notoriété et montrer mon savoir-faire",
            "Confiance (Témoignages/Réalisations)": "rassurer les clients avec mes chantiers",
            "Vente (Demande de devis)": "inciter à prendre contact pour un projet"
        }
        goal_choice = st.selectbox("Objectif du post", list(objectifs.keys()))
        
        if st.button("Générer mon post pro", use_container_width=True):
            if biz:
                with st.spinner("Rédaction en cours..."):
                    st.session_state.result = generate_social_bundle(biz, industry, objectifs[goal_choice])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if "result" in st.session_state:
            st.success("Votre post est prêt !")
            st.markdown(st.session_state.result)
            st.button("📋 Copier le texte")
        else:
            # Image d'illustration pro pour combler le vide
            st.image("https://images.unsplash.com/photo-1541888946425-d81bb19480c5?auto=format&fit=crop&q=80&w=1000", caption="Valorisez vos chantiers avec l'IA")

