import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    st.title("🏛️ Studio de Création")

    # LA LISTE GÉANTE DES MÉTIERS
    metiers = [
        "Maçonnerie / Gros Oeuvre", "Menuiserie / Ebénisterie", "Charpente / Toiture",
        "Plomberie / Chauffage", "Electricité / Domotique", "Peinture / Décoration",
        "Carrelage / Dallage", "Plâtrerie / Isolation", "Paysagiste / Jardinier",
        "Climatisation / PAC", "Serrurerie / Métallerie", "Vitrerie",
        "Cuisine / Bain (Installation)", "Piscine / Spa", "Nettoyage de façade",
        "Diagnostic Immobilier", "Architecture d'intérieur", "Rénovation de Prestige",
        "Ferronnerie d'art", "Taille de pierre", "Ramoneur", "Exterminateur / Nuisibles"
    ]

    col_in, col_out = st.columns([1, 1.2], gap="large")

    with col_in:
        with st.container(border=True):
            biz = st.text_input("Nom de l'entreprise", placeholder="ex: MENUISERIE DU RHÔNE")
            industry = st.selectbox("Sélectionnez votre métier spécialisé", metiers)
            goal = st.selectbox("Objectif", ["Visibilité", "Vente directe", "Confiance"])
            
            if st.button("✨ GÉNÉRER LE PACK", use_container_width=True):
                if biz:
                    with st.spinner("L'IA forge votre contenu..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                else:
                    st.error("Nom requis")

    with col_out:
        if "result" in st.session_state:
            st.markdown(f"""
                <div style="background: white; color: black; padding: 15px; border-radius: 15px;">
                    <div style="display:flex; align-items:center; margin-bottom:10px;">
                        <div style="width:30px; height:30px; background:#6366f1; border-radius:50%; margin-right:10px;"></div>
                        <b>{st.session_state.biz_name}</b>
                    </div>
                    <img src="https://images.unsplash.com/photo-1541888946425-d81bb19480c5?w=600" style="width:100%; border-radius:8px;">
                    <p style="margin-top:10px; font-size:0.9rem;">{st.session_state.result}</p>
                </div>
            """, unsafe_allow_html=True)
