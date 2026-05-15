import streamlit as st

def show():
    st.markdown("""
        <style>
        .stApp { background-color: #000 !important; }
        .hero-section {
            width: 100%;
            height: 450px;
            background: linear-gradient(rgba(0,0,0,0.6), #000), 
                        url('https://images.unsplash.com/photo-1541888946425-d81bb19480c5?q=80&w=2000');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .main-title {
            font-size: 4.5rem;
            font-weight: 900;
            color: white;
            margin: 0;
            letter-spacing: -2px;
        }
        .social-icons-row {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin: 30px 0;
            font-size: 2.5rem;
            color: #6366f1;
        }
        </style>
        <div class="hero-section">
            <h1 class="main-title">GHOSTCONTENT.</h1>
            <p style="color: #6366f1; font-weight: bold; font-size: 1.3rem;">L'ARTISANAT DEVIENT DIGITAL</p>
        </div>
        <div class="social-icons-row">
            <span>📸</span> <span>🎵</span> <span>👥</span> <span>💼</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    _, col_btn, _ = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("🚀 ACCÉDER AU STUDIO PRO", use_container_width=True):
            st.session_state.user = True
            st.rerun()

    st.markdown("""
        <div style="padding: 60px 10%; text-align: center; color: white;">
            <h2 style="font-size: 2.5rem;">Pourquoi votre métier a besoin des réseaux ?</h2>
            <p style="color: #888; font-size: 1.2rem; max-width: 800px; margin: 20px auto;">
                Un chantier non publié est un chantier perdu. GhostContent transforme vos photos en aimants à clients. 
                Optimisé pour Instagram, TikTok et Facebook.
            </p>
        </div>
    """, unsafe_allow_html=True)
