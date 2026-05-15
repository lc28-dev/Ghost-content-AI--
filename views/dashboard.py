import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background-color: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    metiers = [
        "Maçonnerie & Gros Œuvre", "Menuiserie & Ebénisterie", "Charpente & Toiture",
        "Plomberie & Chauffage", "Électricité & Domotique", "Peinture & Déco",
        "Carrelage & Sols", "Plâtrerie & Isolation", "Paysagiste & Jardin",
        "Cuisiniste", "Serrurerie & Ferronnerie", "Rénovation Énergétique",
        "Climatisation / PAC", "Nettoyage de Façade", "Architecture d'intérieur"
    ]

    st.markdown("<h1 style='text-align:center; padding:20px;'>🏛️ STUDIO GHOSTCONTENT</h1>", unsafe_allow_html=True)

    col_in, col_out = st.columns([1, 1], gap="large")

    with col_in:
        with st.container(border=True):
            biz = st.text_input("NOM DE L'ENTREPRISE", placeholder="ex: MENUISERIE DU SUD")
            industry = st.selectbox("CORPS DE MÉTIER", metiers)
            goal = st.selectbox("OBJECTIF DU POST", ["Visibilité", "Vente directe", "Confiance client"])
            
            if st.button("🔥 GÉNÉRER LE POST", use_container_width=True):
                if biz:
                    with st.spinner("Forgeage du contenu..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                else:
                    st.error("Nom requis.")

    with col_out:
        if "result" in st.session_state:
            st.markdown(f"""
                <div style="background: white; color: black; border-radius: 25px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.3);">
                    <div style="padding: 15px; border-bottom: 1px solid #eee; font-weight: bold; display: flex; align-items: center;">
                        <div style="width: 30px; height: 30px; background: #6366f1; border-radius: 50%; margin-right: 10px;"></div>
                        {st.session_state.biz_name.upper()}
                    </div>
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f3344d7?w=800" style="width: 100%;">
                    <div style="padding: 15px; font-size: 0.9rem; line-height: 1.5;">
                        {st.session_state.result}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("📋 COPIER LE TEXTE")
