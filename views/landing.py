import streamlit as st

def show():
    # CSS pour le look "Luxe" et l'image fixe en haut
    st.markdown("""
        <style>
        .stApp { background-color: #050505; }
        
        .hero-bg {
            background-image: url('https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=2000&auto=format&fit=crop');
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 0 0 80px 80px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        
        .hero-card {
            background: rgba(0, 0, 0, 0.7);
            padding: 50px;
            border-radius: 30px;
            backdrop-filter: blur(15px);
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
            max-width: 80%;
        }

        .section-dark {
            padding: 100px 10% 50px 10%;
            background: #050505;
            color: white;
        }

        .benefit-box {
            background: #0f0f0f;
            padding: 40px;
            border-radius: 25px;
            border: 1px solid #1a1a1a;
            transition: 0.3s;
            height: 100%;
        }
        .benefit-box:hover { border-color: #6366f1; transform: translateY(-5px); }
        
        .gold-text {
            background: linear-gradient(90deg, #ffffff, #a1a1a1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 4rem; font-weight: 900;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SECTION 1 : HERO ---
    st.markdown("""
        <div class="hero-bg">
            <div class="hero-card">
                <h1 class="gold-text">GHOSTCONTENT</h1>
                <p style="color: #888; font-size: 1.5rem; font-weight: 300;">L'élite de la communication pour les bâtisseurs de demain.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- SECTION 2 : L'ARGUMENTAIRE ---
    st.markdown('<div class="section-dark">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("<h2 style='font-size: 3rem;'>Le chantier ne s'arrête jamais.</h2>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 1.2rem; color: #999; line-height: 1.8;'>
            Un artisan qui ne publie pas est un artisan qui n'existe pas aux yeux du marché actuel.<br><br>
            <b>Instagram n'est pas un jouet, c'est votre vitrine 24h/24.</b><br>
            C'est là que vos futurs clients décident si vous êtes digne de confiance. GhostContent 
            transforme votre expertise technique en une autorité numérique incontestable.
            </p>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://images.unsplash.com/photo-1541888946425-d81bb19480c5?auto=format&fit=crop&q=80&w=1000")

    st.markdown("<br><br><h2 style='text-align:center;'>Pourquoi nous choisir ?</h2><br>", unsafe_allow_html=True)
    
    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown('<div class="benefit-box"><h3>Confiance Totale</h3><p>Montrez vos finitions et rassurez vos prospects avant le premier appel.</p></div>', unsafe_allow_html=True)
    with b2:
        st.markdown('<div class="benefit-box"><h3>Gain de Temps</h3><p>Générez vos scripts et visuels en 30 secondes après votre journée.</p></div>', unsafe_allow_html=True)
    with b3:
        st.markdown('<div class="benefit-box"><h3>Prestige</h3><p>Distinguez-vous de la concurrence avec un contenu haut de gamme.</p></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("✨ LANCER LE GÉNÉRATEUR", use_container_width=True):
        st.session_state.user = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
