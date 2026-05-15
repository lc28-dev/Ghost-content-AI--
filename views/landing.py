import streamlit as st

def show():
    # Style injecté proprement pour ne pas s'afficher en texte
    st.markdown("""
        <style>
        .stApp { background-color: #000 !important; }
        .main { background-color: #000 !important; }
        
        /* Bannière Full Screen */
        .hero-banner {
            width: 100%;
            height: 400px;
            background: linear-gradient(rgba(0,0,0,0.6), #000), 
                        url('https://images.unsplash.com/photo-1541888946425-d81bb19480c5?q=80&w=2000');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            border-bottom: 1px solid #222;
        }

        .big-title {
            font-size: 4rem;
            font-weight: 900;
            color: white;
            letter-spacing: -2px;
            margin: 0;
        }

        /* Logos Réseaux Sociaux */
        .social-box {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin: 30px 0;
            font-size: 2.5rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Affichage de la bannière
    st.markdown("""
        <div class="hero-banner">
            <h1 class="big-title">GHOSTCONTENT.</h1>
            <p style="color: #6366f1; font-weight: bold; font-size: 1.2rem;">L'ÉLITE DU CONTENU ARTISAN</p>
        </div>
        <div class="social-box">
            <span>📸</span> <span>🎵</span> <span>👥</span> <span>💼</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bouton au milieu
    _, col_btn, _ = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🔥 LANCER LE STUDIO PRO", use_container_width=True):
            st.session_state.user = True
            st.rerun()

    # Section dynamique
    st.markdown("""
        <div style="padding: 50px 10%; text-align: center;">
            <h2 style="color: white; font-size: 2.5rem;">Pourquoi votre métier a besoin d'Instagram ?</h2>
            <p style="color: #888; font-size: 1.2rem;">
                80% des clients vérifient vos réseaux avant de signer. Ne soyez plus invisible.
            </p>
        </div>
    """, unsafe_allow_html=True)
