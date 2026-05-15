import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background-color: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    # LISTE MASSIVE DES MÉTIERS
    metiers = [
        "Maçonnerie / Gros Œuvre", "Menuiserie d'Art", "Charpente & Couverture",
        "Plomberie & Chauffage", "Électricité & Domotique", "Peinture & Déco",
        "Carrelage & Dallage", "Plâtrerie & Isolation", "Paysagiste & Espaces Verts",
        "Piscine & Spa", "Climatisation & PAC", "Serrurerie & Ferronnerie",
        "Architecture d'Intérieur", "Cuisiniste", "Poseur de Sols", "Vitrerie",
        "Rénovation Énergétique", "Nettoyage Haute Pression", "Ramoneur",
        "Exterminateur Professionnel", "Tailleur de Pierre", "Artisan Photographe"
    ]

    st.markdown("<h1 style='text-align:center; font-size: 3rem; font-weight: 900;'>STUDIO DE CRÉATION.</h1>", unsafe_allow_html=True)
    
    col_form, col_render = st.columns([1, 1], gap="large")

    with col_form:
        st.markdown("### 🛠 Configuration")
        with st.container(border=True):
            biz = st.text_input("NOM DE L'ENSEIGNE", placeholder="ex: GUILLIN MAÇONNERIE")
            industry = st.selectbox("VOTRE MÉTIER", metiers)
            goal = st.selectbox("OBJECTIF DU POST", ["Visibilité Explosive", "Signature de Devis", "Preuve Sociale"])
            
            if st.button("GÉNÉRER LE PACK COMPLET", use_container_width=True):
                if biz:
                    with st.spinner("L'IA forge votre image de marque..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                        # On assigne une image en fonction du métier
                        st.session_state.img_url = "https://images.unsplash.com/photo-1541888946425-d81bb19480c5?w=800"
                else:
                    st.error("Veuillez renseigner le nom.")

    with col_render:
        if "result" in st.session_state:
            st.markdown("### 📱 Rendu Instagram")
            # Simulation Smartphone
            st.markdown(f"""
                <div style="background: #fff; color: #000; border-radius: 30px; padding: 20px; box-shadow: 0 30px 60px rgba(255,255,255,0.1);">
                    <div style="display:flex; align-items:center; margin-bottom:15px;">
                        <div style="width:40px; height:40px; border-radius:50%; background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); margin-right:10px;"></div>
                        <span style="font-weight: 800;">{st.session_state.biz_name.upper()}</span>
                    </div>
                    <img src="{st.session_state.img_url}" style="width:100%; border-radius:15px; margin-bottom:15px;">
                    <div style="font-size: 0.9rem; line-height: 1.6;">
                        {st.session_state.result}
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("COPIER POUR LE TÉLÉPHONE")
