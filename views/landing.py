import streamlit as st

def show():
    st.markdown("""
        <style>
        .stApp { background-color: #050505; }
        
        .hero-title {
            font-size: 5rem; font-weight: 900; text-align: center;
            background: linear-gradient(to right, #ffffff, #666666);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-top: 50px; line-height: 1;
        }
        
        .section-box {
            padding: 100px 20px; text-align: center; color: white;
        }

        .benefit-card {
            background: #111; border: 1px solid #222; padding: 40px;
            border-radius: 30px; transition: 0.4s; text-align: left;
        }
        .benefit-card:hover { border-color: #6366f1; transform: translateY(-10px); }

        .big-text { font-size: 1.8rem; color: #999; line-height: 1.6; max-width: 900px; margin: 0 auto; }
        
        .cta-btn {
            background: white; color: black; padding: 20px 40px;
            border-radius: 50px; font-weight: bold; font-size: 1.2rem;
            text-decoration: none; display: inline-block; margin-top: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    # HEADER
    st.markdown('<h1 class="hero-title">DOMINEZ VOTRE<br>MARCHÉ LOCAL.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="big-text" style="text-align:center; margin-top:20px;">Transformez votre savoir-faire en une marque de prestige sur les réseaux sociaux.</p>', unsafe_allow_html=True)
    
    if st.button("DÉMARRER LA CRÉATION", use_container_width=True):
        st.session_state.user = True
        st.rerun()

    st.markdown("---")

    # ARGUMENTAIRE RÉSEAUX SOCIAUX
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("<h2 style='color:white; font-size:3rem;'>Pourquoi vos mains ne suffisent plus ?</h2>", unsafe_allow_html=True)
        st.write("""
        <p style='color:#888; font-size:1.2rem;'>
        Aujourd'hui, le chantier ne s'arrête pas quand vous posez vos outils. 
        Il s'arrête quand le monde entier voit ce que vous avez été capable de construire.<br><br>
        Un compte Instagram actif, c'est :<br>
        <b>• Une preuve de confiance :</b> Vos clients voient vos finitions avant même de vous appeler.<br>
        <b>• Un filtre anti-curieux :</b> Vous attirez des chantiers à haute valeur ajoutée.<br>
        <b>• Une avance définitive :</b> Pendant que vos concurrents dorment, vous occupez l'espace numérique.
        </p>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1534398079244-67c8ad85592e?q=80&w=1000&auto=format&fit=crop")

    # CARDS
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="benefit-card"><h3>SCALABILITÉ</h3><p>Ne courez plus après les clients. Laissez-les venir à vous grâce à une image de marque irréprochable.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="benefit-card"><h3>RÉPUTATION</h3><p>Chaque post est une brique de plus dans la forteresse de votre e-réputation locale.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="benefit-card"><h3>VITESSE</h3><p>Produisez en 30 secondes ce qui prendrait 4 heures à une agence de communication.</p></div>', unsafe_allow_html=True)
