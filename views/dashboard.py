import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align:center;'>🏛️ Studio GhostContent</h1>", unsafe_allow_html=True)
    
    col_input, col_preview = st.columns([1, 1], gap="large")

    with col_input:
        st.markdown("### Configuration")
        with st.container(border=True):
            biz = st.text_input("Nom de l'entreprise", placeholder="ex: GUILLIN MAÇONNERIE")
            industry = st.selectbox("Votre métier", ["Rénovation Prestige", "Charpente & Bois", "Gros Œuvre", "Design Intérieur"])
            goal = st.selectbox("Objectif stratégique", ["Visibilité (Nouveaux clients)", "Vente (Signer des devis)"])
            
            if st.button("🔥 GÉNÉRER LE PACK", use_container_width=True):
                if biz:
                    with st.spinner("L'IA forge votre contenu..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                        st.session_state.ind_name = industry
                else:
                    st.error("Veuillez entrer un nom.")

    with col_preview:
        st.markdown("### Aperçu du Post")
        if "result" in st.session_state:
            # Cadre style Instagram
            st.markdown(f"""
                <div style="background: white; color: black; padding: 20px; border-radius: 20px; border: 1px solid #ddd;">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <div style="width: 40px; height: 40px; background: #6366f1; border-radius: 50%; margin-right: 10px;"></div>
                        <b>{st.session_state.biz_name.lower().replace(' ', '_')}</b>
                    </div>
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f3344d7?q=80&w=1080" style="width: 100%; border-radius: 10px; margin-bottom: 15px;">
                    <p style="font-size: 0.9rem; line-height: 1.4;">{st.session_state.result[:250]}...</p>
                    <p style="color: #999; font-size: 0.8rem;">Voir la suite...</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("Voir le texte complet à copier"):
                st.write(st.session_state.result)
                st.button("📋 Copier le texte")
        else:
            st.info("Le rendu de votre post apparaîtra ici après génération.")
