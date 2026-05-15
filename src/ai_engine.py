from groq import Groq
import os
import streamlit as st

def generate_social_bundle(business_name, industry, goal):
    # On récupère la clé. Si elle n'existe pas, on met une valeur vide pour éviter le crash
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    
    if not api_key:
        return "⚠️ Erreur : La clé API 'GROQ_API_KEY' n'est pas configurée dans Streamlit."

    client = Groq(api_key=api_key)
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", # MODÈLE MIS À JOUR ICI
            messages=[{"role": "user", "content": f"Rédige un post pro pour {business_name} ({industry}) - But: {goal}"}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur IA : {str(e)}"
