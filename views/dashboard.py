import streamlit as st

def show():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
        .stApp { background-color: #020202; }
        
        /* Section Impact Haut */
        .hero-header {
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.8)), 
                        url('https://images.unsplash.com/photo-1531834357221-dc767329742c?q=80&w=2000&auto=format&fit=crop');
            background-size: cover;
            background-position: center;
            height: 700px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .title-main {
            font-size: 5rem; font-weight: 900; color: white;
            letter-spacing: -2px; margin-bottom: 10px;
            text-shadow: 0 10px 30px rgba(0,0,0,1);
        }

        /* Barre Sociale Dynamique */
        .social-strip {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            padding: 20px 0;
            display: flex;
            justify-content: center;
            gap: 60px;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin-top: -30px;
        }
        .social-strip i { font-size: 2.5rem; color: #fff; transition: 0.3s; }
        .social-strip i:hover { color: #6366f1; transform: scale(1.2); }

        /* Bouton Action Ultra */
        .stButton>button {
            background: #fff; color: #000;
            border-radius: 50px; padding: 20px 50px;
            font-size: 1.3rem; font-weight: 800; border: none;
            box-shadow: 0 10px 40px rgba(255,255,255,0.2);
        }
        </style>

        <div class="hero-header">
            <h1 class="title-main">GHOSTCONTENT.</h1>
            <p style="color: #6366f1; font-size: 1.5rem; font-weight: 700; text-transform: uppercase; letter-spacing: 5px;">
                Domination Digitale Artisanale
            </p>
        </div>
        
        <div class="social-strip">
            <i class="fab fa-instagram"></i>
            <i class="fab fa-tiktok"></i>
            <i class="fab fa-facebook-f"></i>
            <i class="fab fa-linkedin-in"></i>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    col_l, col_btn, col_r = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("ACCÉDER AU STUDIO →", use_container_width=True):
            st.session_state.user = True
            st.rerun()

    st.markdown("""
        <div style="text-align:center; padding: 100px 5%;">
            <h2 style="font-size: 3rem; color: #fff;">Votre savoir-faire mérite l'excellence visuelle.</h2>
            <p style="color: #666; font-size: 1.4rem; max-width: 800px; margin: 0 auto;">
                Arrêtez de poster des photos banales sans stratégie. GhostContent utilise l'IA pour créer des récits 
                qui transforment vos abonnés en clients fidèles.
            </p>
        </div>
    """, unsafe_allow_html=True)
