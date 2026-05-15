import streamlit as st

def show():
    # CSS pour le look Élite
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
        .stApp { background-color: #050505; }
        
        .hero-banner {
            width: 100%;
            height: 500px;
            background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                        url('https://images.unsplash.com/photo-1504307651254-35680f3344d7?q=80&w=2000');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            border-bottom: 2px solid #1a1a1a;
        }

        .social-bar {
            display: flex;
            justify-content: center;
            gap: 50px;
            margin: 50px 0;
            font-size: 3rem;
            color: #6366f1;
        }

        .section-text {
            padding: 60px 10%;
            color: white;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # BANNIÈRE
    st.markdown("""
        <div class="hero-banner">
            <h1 style='color:white; font-size:4.5rem; font-weight:900; margin:0;'>GHOSTCONTENT</h1>
            <p style='color:#6366f1; font-size:1.8rem; font-weight:bold;'>L'IA AU SERVICE DES BÂTISSEURS</p>
        </div>
    """, unsafe_allow_html=True)

    # BOUTON CENTRAL
    col1, col_btn, col3 = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("🚀 ACCÉDER AU GÉNÉRATEUR", use_container_width=True, type="primary"):
            st.session_state.user = True
            st.rerun()

    # LOGOS RÉSEAUX SOCIAUX (Vrais icônes)
    st.markdown("""
        <div class="social-bar">
            <i class="fab fa-instagram"></i>
            <i class="fab fa-tiktok"></i>
            <i class="fab fa-facebook"></i>
            <i class="fab fa-linkedin"></i>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-text"><h2>Vos chantiers sont vos meilleures publicités.</h2><p style="color:#888;">Ne laissez plus vos concurrents prendre la place sur Instagram. Montrez votre savoir-faire dès maintenant.</p></div>', unsafe_allow_html=True)
