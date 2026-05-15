import streamlit as st

def show():
    # CSS AVANCÉ : Effet Parallaxe et Design Long
    st.markdown("""
        <style>
        /* Image de fond fixe en haut */
        .hero-bg {
            background-image: url('https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=2000&auto=format&fit=crop');
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            height: 500px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            border-radius: 0 0 50px 50px;
        }
        
        .hero-text {
            background: rgba(15, 23, 42, 0.7);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            text-align: center;
            border: 1px solid rgba(255,255,255,0.1);
        }

        /* Section Contenu qui remonte sur l'image */
        .content-section {
            background: #0f172a;
            padding: 60px 20px;
            margin-top: -50px;
            border-radius: 50px 50px 0 0;
        }

        .feature-card {
            background: #1e293b;
            padding: 30px;
            border-radius: 20px;
            border-left: 5px solid #6366f1;
            margin-bottom: 20px;
        }
        
        h2 { color: #818cf8; font-size: 2.5rem !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- SECTION 1 : HERO (L'IMAGE FIXE) ---
    st.markdown("""
        <div class="hero-bg">
            <div class="hero-text">
                <h1 style='color:white; font-size: 3.5rem; font-weight:900;'>GHOSTCONTENT</h1>
                <p style='color:#cbd5e1; font-size:1.5rem;'>L'Art de la Visibilité pour les Artisans</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- SECTION 2 : POURQUOI LES RÉSEAUX ? (LE CONTENU LONG) ---
    with st.container():
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("## Pourquoi votre métier a besoin d'Instagram ?")
            st.write("""
                Un artisan qui ne montre pas ses chantiers est un artisan invisible. 
                Aujourd'hui, **80% des clients** vérifient le compte Instagram ou Facebook d'une entreprise 
                avant de signer un devis. 
                
                **GhostContent vous permet de :**
                - Montrer la qualité de vos finitions.
                - Créer un lien de confiance immédiat.
                - Transformer vos simples photos de chantier en machines à vendre.
            """)
        with col2:
            st.image("https://images.unsplash.com/photo-1504307651254-35680f3344d7?q=80&w=1000&auto=format&fit=crop")

        st.divider()

        # --- SECTION 3 : LES AVANTAGES ---
        st.markdown("<h2 style='text-align:center;'>La puissance de l'IA à votre service</h2>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="feature-card"><h3>Gain de Temps</h3><p>Ne passez plus 1h à chercher vos mots après une journée de chantier.</p></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="feature-card"><h3>Professionnalisme</h3><p>Des textes sans fautes, percutants et adaptés aux algorithmes TikTok/Insta.</p></div>', unsafe_allow_html=True)
        with c3:
            st.markdown('<div class="feature-card"><h3>Plus de Devis</h3><p>Chaque post est optimisé pour pousser le client à vous appeler.</p></div>', unsafe_allow_html=True)

        # --- SECTION 4 : L'APPEL À L'ACTION ---
        st.divider()
        st.markdown("<h2 style='text-align:center;'>Prêt à dominer votre secteur ?</h2>", unsafe_allow_html=True)
        
        col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
        with col_btn2:
            if st.button("✨ ACCÉDER AU GÉNÉRATEUR GRATUIT", use_container_width=True):
                st.session_state.user = True
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
