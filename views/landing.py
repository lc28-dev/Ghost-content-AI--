import streamlit as st

def show():
    st.markdown("""
        <style>
        .stApp { background-color: #050505; }
        
        /* Bannière Largeur Totale */
        .full-banner {
            width: 100%;
            height: 450px;
            background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                              url('https://images.unsplash.com/photo-1541888946425-d81bb19480c5?q=80&w=2000');
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            border-radius: 0 0 40px 40px;
            margin-bottom: 50px;
        }

        .social-icons {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 40px 0;
            font-size: 2rem;
        }

        .cta-button {
            background: #6366f1;
            color: white;
            padding: 15px 35px;
            border-radius: 12px;
            font-weight: bold;
            text-decoration: none;
            transition: 0.3s;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- BANNIÈRE HAUTE ---
    st.markdown("""
        <div class="full-banner">
            <h1 style='color:white; font-size:4rem; font-weight:900; text-align:center;'>GHOSTCONTENT</h1>
            <p style='color:#ddd; font-size:1.5rem;'>L'agence digitale automatique des artisans</p>
            <br>
        </div>
    """, unsafe_allow_html=True)

    # --- BOUTON CENTRAL ---
    col_l, col_btn, col_r = st.columns([1, 1.5, 1])
    with col_btn:
        if st.button("🚀 LANCER LE GÉNÉRATEUR", use_container_width=True, type="primary"):
            st.session_state.user = True
            st.rerun()

    # --- LOGOS SOCIAUX DYNAMIQUES ---
    st.markdown("""
        <div class="social-icons">
            <span title="Instagram">📸</span>
            <span title="TikTok">🎵</span>
            <span title="Facebook">👥</span>
            <span title="LinkedIn">💼</span>
        </div>
        <p style='text-align:center; color:#666;'>Optimisé pour tous vos réseaux</p>
    """, unsafe_allow_html=True)

    st.divider()

    # --- CONTENU ---
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://images.unsplash.com/photo-1504307651254-35680f3344d7?q=80&w=800")
    with c2:
        st.markdown("## Ne soyez plus l'artisan fantôme.")
        st.write("Vos futurs clients sont sur leur téléphone. Montrez-leur votre savoir-faire avec des scripts de posts professionnels générés en 3 secondes.")
