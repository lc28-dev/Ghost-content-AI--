import streamlit as st
from views import landing, dashboard

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user:
    dashboard.show()
else:
    landing.show()
