import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    # CSS pour fond dégradé sombre et cartes lumineuses
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%);
        }
        .main-header {
            background: linear-gradient(90deg, #818cf8, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem;
            font-weight: 900;
            text-align: center;
            margin-bottom: 0px;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 25px;
            padding: 30px;
            backdrop-filter: blur(10px);
        }
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            border: none; color: white; border-radius: 12px;
            padding: 15px; font-weight: 800; font-size: 1.2rem;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">GHOSTCONTENT PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#94a3b8; font-size:1.2rem; margin-bottom:40px;">L\'élite de l\'IA pour les artisans du futur.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("⚙️ Configuration")
        biz = st.text_input("Nom de l'entreprise", placeholder="ex: Guillin Maçonnerie")
        
        industry = st.selectbox("Votre expertise", [
            "Maçonnerie & Gros Œuvre", "Menuiserie d'Art", "Plomberie Haute Précision", 
            "Électricité Connectée", "Peinture & Design", "Paysagisme de Luxe"
        ])
        
        goal = st.selectbox("Objectif stratégique", [
            "Exploser ma Visibilité", "Vendre mes chantiers", "Rassurer (Preuve sociale)"
        ])
        
        if st.button("✨ GÉNÉRER LE SCRIPT", use_container_width=True):
            if biz:
                with st.spinner("L'IA Ghost rédige votre succès..."):
                    st.session_state.result = generate_social_bundle(biz, industry, goal)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Image pro de réseaux sociaux
        st.image("https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
        
        if "result" in st.session_state:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.success("Post prêt à copier ✅")
            st.markdown(st.session_state.result)
            st.markdown('</div>', unsafe_allow_html=True)
