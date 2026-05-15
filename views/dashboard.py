import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.markdown("<style>.stApp { background: #050505; color: white; }</style>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='text-align:center; padding: 20px;'>🏛️ STUDIO DE CRÉATION</h1>", unsafe_allow_html=True)
    
    col_in, col_out = st.columns([1, 1.2], gap="large")

    with col_in:
        with st.container(border=True):
            st.subheader("🛠️ Votre Chantier")
            biz = st.text_input("Nom de l'entreprise", placeholder="ex: MENUISERIE DU RHÔNE")
            industry = st.selectbox("Domaine d'expertise", ["Rénovation Maison", "Gros Œuvre / Maçonnerie", "Menuiserie / Bois", "Électricité / Domotique"])
            goal = st.selectbox("Objectif du post", ["Se faire connaître (Visibilité)", "Rassurer le client (Confiance)", "Appel au devis (Vente)"])
            
            if st.button("✨ GÉNÉRER LE POST PRO", use_container_width=True):
                if biz:
                    with st.spinner("Rédaction en cours..."):
                        st.session_state.result = generate_social_bundle(biz, industry, goal)
                        st.session_state.biz_name = biz
                else:
                    st.error("Entrez le nom de l'entreprise.")

    with col_out:
        if "result" in st.session_state:
            st.subheader("📸 Rendu Final")
            # Simulation d'un post Instagram réaliste
            st.markdown(f"""
                <div style="background: white; color: black; padding: 0px; border-radius: 15px; overflow: hidden; border: 1px solid #ddd;">
                    <div style="padding: 10px; display: flex; align-items: center; border-bottom: 1px solid #eee;">
                        <div style="width: 32px; height: 32px; background: #6366f1; border-radius: 50%; margin-right: 10px;"></div>
                        <span style="font-weight: bold; font-size: 0.9rem;">{st.session_state.biz_name.lower().replace(' ','_')}</span>
                    </div>
                    <img src="https://images.unsplash.com/photo-1503387762-592dee58c460?q=80&w=1000" style="width: 100%; display: block;">
                    <div style="padding: 15px;">
                        <p style="font-size: 0.9rem; line-height: 1.5; color: #222;">{st.session_state.result}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.button("📋 Copier pour Instagram / Facebook")
        else:
            # Image d'attente pro
            st.image("https://images.unsplash.com/photo-1541888946425-d81bb19480c5?q=80&w=1000", caption="Vos futurs posts ressembleront à ça.")
