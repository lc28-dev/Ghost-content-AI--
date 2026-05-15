import streamlit as st

def show():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
        .stApp { background-color: #000; }
        .hero {
            height: 600px;
            background: linear-gradient(rgba(0,0,0,0.5), #000), 
                        url('https://images.unsplash.com/photo-1541888946425-d81bb19480c5?q=80&w=2000');
            background-size: cover; background-position: center;
            display: flex; flex-direction: column; justify-content: center; align-items: center;
        }
        .main-title { font-size: 5rem; font-weight: 900; color: white; margin: 0; }
        .social-icons { margin: 40px 0; display: flex; gap: 40px; font-size: 2.5rem; color: #6366f1; }
        .stButton>button { 
            background: #6366f1; color: white; border-radius: 50px; 
            padding: 20px 60px; font-weight: bold; border: none; font-size: 1.2rem;
        }
        </style>
        <div class="hero">
            <h1 class="main-title">GHOSTCONTENT</h1>
            <p style="color:#aaa; font-size:1.5rem;">L'IA qui construit votre réputation.</p>
            <div class="social-icons">
                <i class="fab fa-instagram"></i>
                <i class="fab fa-tiktok"></i>
                <i class="fab fa-facebook"></i>
                <i class="fab fa-whatsapp"></i>
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, btn, c3 = st.columns([1,2,1])
    with btn:
        if st.button("🚀 ACCÉDER AU STUDIO PRO", use_container_width=True):
            st.session_state.user = True
            st.rerun()
