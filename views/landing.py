import streamlit as st

def show():
    # Style CSS personnalisé pour un look épuré
    st.markdown("""
        <style>
        .main-title { font-size: 3rem; font-weight: 800; letter-spacing: -1px; text-align: center; color: white; margin-bottom: 0; }
        .sub-title { font-size: 1.2rem; text-align: center; color: #94a3b8; margin-bottom: 2rem; }
        .hero-card { background: #1e293b; padding: 2rem; border-radius: 1rem; border: 1px solid #334155; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="main-title">GhostContent</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">L\'intelligence artificielle au service de votre croissance sociale.</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container(border=True):
            st.markdown("### Commencez maintenant")
            st.write("Générez des posts optimisés pour LinkedIn, Instagram et Twitter en quelques secondes.")
            if st.button("Accéder à l'interface", use_container_width=True):
                st.session_state.user = True
                st.rerun()
