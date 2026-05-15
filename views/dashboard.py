import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    # CSS AVANCÉ POUR DESIGN PREMIUM
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        }
        .hero-section {
            padding: 40px 20px;
            text-align: center;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .title-gradient {
            background: linear-gradient(90deg, #6366f1, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
        }
        .card-pro {
            background: rgba(30, 41, 59, 0.7);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(99, 102, 241, 0.3);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    # HEADER DE PRÉSENTATION
    st.markdown("""
        <div class="hero-section">
            <h1 class="title-gradient">GhostContent Pro</h1>
            <p style="font-size: 1.4rem; color: #94a3b8; max-width: 800px; margin: 0 auto;">
                L'outil d'élite pour les artisans qui veulent dominer les réseaux sociaux. 
                Ne perdez plus de temps à écrire, montrez votre talent. 
                <b>Propulsé par l'IA la plus puissante du marché.</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="card-pro">', unsafe_allow_html=True)
        st.subheader("⚒️ Configuration du Post")
        
        biz = st.text_input("Nom de l'entreprise", placeholder="ex: Guillin Maçonnerie")
        
        industry = st.selectbox("Votre métier d'expert", [
            "Maçonnerie & Gros Œuvre", "Menuiserie & Agencement", 
            "Plomberie & Chauffage", "Électricité Générale", 
            "Peinture & Finition", "Paysagisme & Jardin", 
            "Rénovation de Prestige", "Architecture & Design"
        ])
        
        goal = st.selectbox("Objectif stratégique", [
            "Visibilité Totale (Attirer de nouveaux regards)",
            "Preuve de Qualité (Photos de chantiers / Avis)",
            "Conversion Directe (Prise de contact / Devis)"
        ])
        
        st.write("---")
        if st.button("🚀 GÉNÉRER MON CONTENU", use_container_width=True):
            if biz:
                with st.spinner("L'IA Ghost analyse votre métier..."):
                    st.session_state.result = generate_social_bundle(biz, industry, goal)
            else:
                st.warning("Entrez le nom de votre entreprise.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # IMAGE STYLE TÉLÉPHONE / RÉSEAUX SOCIAUX
        st.markdown("""
            <div style="text-align: center;">
                <img src="https://img.freepik.com/free-vector/social-media-icons-floating_52683-34744.jpg" width="100%" style="border-radius: 20px; margin-bottom: 20px;">
            </div>
        """, unsafe_allow_html=True)

        if "result" in st.session_state:
            st.markdown('<div class="card-pro" style="border-color: #22c55e;">', unsafe_allow_html=True)
            st.success("✨ Post optimisé prêt à l'emploi")
            st.markdown(st.session_state.result)
            if st.button("📋 Copier pour Instagram / Facebook", use_container_width=True):
                st.balloons()
            st.markdown('</div>', unsafe_allow_html=True)
