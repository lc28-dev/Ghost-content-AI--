import streamlit as st

def show():
    st.markdown("""
        <style>
        .stApp { background-color: #050505; }
        
        .hero-header {
            text-align: center;
            padding: 80px 20px 40px 20px;
        }

        .gold-title {
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 900;
            background: linear-gradient(to bottom, #ffffff 30%, #444444 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            margin-bottom: 20px;
        }

        .cta-container {
            display: flex;
            justify-content: center;
            margin-bottom: 60px;
        }

        .section-content {
            background: #0a0a0a;
            padding: 60px 5%;
            border-radius: 40px;
            border: 1px solid #111;
        }

        .benefit-card {
            background: #111;
            padding: 30px;
            border-radius: 20px;
            border-bottom: 4px solid #6366f1;
            height: 100%;
        }

        img { border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER & BOUTON CENTRAL ---
    st.markdown('<div class="hero-header">', unsafe_allow_html=True)
    st.markdown('<h1 class="gold-title">DOMINEZ VOTRE<br>SECTEUR.</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#888; font-size:1.3rem; margin-bottom:30px;">L\'IA qui transforme vos chantiers en vitrines de luxe.</p>', unsafe_allow_html=True)
    
    col_l, col_btn, col_r = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 LANCER LE GÉNÉRATEUR MAINTENANT", use_container_width=True, type="primary"):
            st.session_state.user = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- SECTION ARGUMENTAIRE ---
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown("<h2 style='color:white; font-size:2.5rem;'>Vos chantiers méritent d'être vus.</h2>", unsafe_allow_html=True)
        st.write("""
        <p style='color:#bbb; font-size:1.1rem;'>
        Aujourd'hui, un client ne signe pas un devis sans avoir vu votre travail sur son téléphone. 
        Si vous ne publiez pas, vous n'existez pas.<br><br>
        <b>GhostContent</b> s'occupe de la partie chiante : l'écriture et la stratégie. 
        Vous prenez les photos, on s'occupe du reste.
        </p>
        """, unsafe_allow_html=True)
        # Image de matos pro (Perceuse/Chantier propre)
        st.image("https://images.unsplash.com/photo-1581141849291-1125c7b692b5?q=80&w=1000&auto=format&fit=crop")
    
    with c2:
        # Image de résultat (Rénovation luxe/Cuisine)
        st.image("https://images.unsplash.com/photo-1556912177-c54030639814?q=80&w=1000&auto=format&fit=crop")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="benefit-card">
            <h3 style='color:white;'>+40% de devis signés</h3>
            <p style='color:#888;'>Une présence Instagram soignée rassure vos prospects et justifie vos tarifs premium.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
