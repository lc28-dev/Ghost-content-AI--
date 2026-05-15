import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background: #050505; }</style>", unsafe_allow_html=True)
    
    st.title("🏛️ Studio de Création")
    
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### Votre Projet")
        biz = st.text_input("Nom de l'entreprise", placeholder="ex: LUXE MAÇONNERIE")
        industry = st.selectbox("Domaine d'expertise", ["Rénovation Premium", "Gros Oeuvre", "Design Extérieur"])
        goal = st.selectbox("Objectif", ["Visibilité Maximale", "Signature de Devis"])
        
        if st.button("GÉNÉRER LE PACK COMPLET", use_container_width=True):
            if biz:
                with st.spinner("L'IA forge votre image..."):
                    st.session_state.result = generate_social_bundle(biz, industry, goal)
                    st.session_state.biz_name = biz
            else:
                st.error("Nom requis.")

    with col2:
        if "result" in st.session_state:
            st.markdown("### Aperçu du Post")
            # Simulation d'un post Instagram
            st.markdown(f"""
            <div style="background: white; color: black; padding: 15px; border-radius: 10px;">
                <p><b>@{st.session_state.biz_name.lower().replace(' ','_')}</b></p>
                <img src="https://images.unsplash.com/photo-1541888946425-d81bb19480c5?auto=format&fit=crop&q=80&w=1080" style="width:100%; border-radius:5px;">
                <p style="margin-top:10px;">{st.session_state.result[:200]}...</p>
            </div>
            """, unsafe_allow_html=True)
            st.button("Copier le texte complet")
