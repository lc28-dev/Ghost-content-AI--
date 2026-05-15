import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background-color: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    # LISTE TOTALE DES MÉTIERS
    metiers = [
        "Maçonnerie & Gros Œuvre", "Menuiserie & Agencement", "Charpente & Toiture",
        "Plomberie & Chauffage", "Électricité & Domotique", "Peinture & Ravalement",
        "Carrelage & Sols", "Plâtrerie & Isolation", "Paysagiste & Piscine",
        "Architecture d'Intérieur", "Cuisiniste", "Serrurerie & Métallerie",
        "Énergies Renouvelables", "Nettoyage Industriel", "Expertise Bâtiment"
    ]

    st.title("🏛️ Studio GhostContent")

    col_in, col_out = st.columns([1, 1], gap="large")

    with col_in:
        with st.container(border=True):
            biz = st.text_input("NOM DE VOTRE ENTREPRISE", placeholder="ex: LUXE BÂTIMENT")
            industry = st.selectbox("VOTRE MÉTIER", metiers)
            goal = st.selectbox("OBJECTIF", ["Visibilité", "Signature Devis", "Recrutement"])
            
            if st.button("🚀 GÉNÉRER MON CONTENU PRO", use_container_width=True):
                if biz:
                    with st.spinner("L'IA forge votre post..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                else:
                    st.error("Précisez le nom de l'entreprise.")

    with col_out:
        if "result" in st.session_state:
            st.markdown(f"""
                <div style="background: white; color: black; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.5);">
                    <div style="padding: 15px; border-bottom: 1px solid #eee; font-weight: 900;">
                        📱 {st.session_state.biz_name.upper()}
                    </div>
                    <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=800" style="width: 100%;">
                    <div style="padding: 20px; font-size: 0.9rem; line-height: 1.5;">
                        {st.session_state.result}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("📋 Copier pour Instagram")
