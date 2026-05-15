import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    # Dictionnaire d'images par métier pour que ce soit cohérent
    images_metiers = {
        "Maçonnerie / Gros Oeuvre": "https://images.unsplash.com/photo-1541888946425-d81bb19480c5?w=800",
        "Menuiserie / Ebénisterie": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=800",
        "Plomberie / Chauffage": "https://images.unsplash.com/photo-1581244276891-9979c4c7c821?w=800",
        "Electricité / Domotique": "https://images.unsplash.com/photo-1621905235294-7500bed49cb3?w=800",
        "Peinture / Décoration": "https://images.unsplash.com/photo-1589930750379-b41af141555d?w=800",
        "Paysagiste / Jardinier": "https://images.unsplash.com/photo-1558905617-15456d50ff4a?w=800",
        "Piscine / Spa": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=800",
        "Ferronnerie d'art": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?w=800"
    }

    st.title("🏛️ Studio de Création Pro")

    col_in, col_out = st.columns([1, 1.2], gap="large")

    with col_in:
        with st.container(border=True):
            biz = st.text_input("Nom de l'entreprise", placeholder="ex: LUXE RÉNOVATION")
            industry = st.selectbox("Sélectionnez votre corps de métier", list(images_metiers.keys()) + ["Autre"])
            goal = st.selectbox("Objectif", ["Visibilité", "Vente", "Confiance"])
            
            if st.button("🔥 GÉNÉRER MON POST", use_container_width=True):
                if biz:
                    with st.spinner("L'IA génère le texte et l'image..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                        # On récupère l'image correspondante
                        st.session_state.post_img = images_metiers.get(industry, "https://images.unsplash.com/photo-1503387762-592dee58c460?w=800")
                else:
                    st.error("Veuillez entrer le nom de l'entreprise.")

    with col_out:
        if "result" in st.session_state:
            # RENDU DU POST (Look Instagram)
            st.markdown(f"""
                <div style="background: white; color: black; border-radius: 20px; overflow: hidden; border: 1px solid #ddd;">
                    <div style="padding: 15px; display: flex; align-items: center; border-bottom: 1px solid #eee;">
                        <div style="width: 35px; height: 35px; background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); border-radius: 50%; margin-right: 10px;"></div>
                        <span style="font-weight: bold;">{st.session_state.biz_name.upper()}</span>
                    </div>
                    <img src="{st.session_state.post_img}" style="width: 100%; display: block;">
                    <div style="padding: 20px;">
                        <p style="font-size: 0.95rem; line-height: 1.5; color: #111;">{st.session_state.result}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("📋 Copier pour Instagram")
