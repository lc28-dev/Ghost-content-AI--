import os
from groq import Groq
import streamlit as st

def generate_social_bundle(business_name, industry, goal):
    # Récupération de la clé API depuis les secrets Streamlit
    api_key = st.secrets.get("GROQ_API_KEY")
    
    if not api_key:
        return "Erreur : La clé GROQ_API_KEY n'est pas configurée dans les Secrets."

    client = Groq(api_key=api_key)
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Tu es un expert marketing spécialisé dans l'artisanat de luxe."},
                {"role": "user", "content": f"Rédige un post captivant pour {business_name} spécialisé en {industry}. L'objectif est {goal}. Utilise un ton pro et des emojis."}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur technique : {str(e)}"
