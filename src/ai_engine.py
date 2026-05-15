import os
from groq import Groq
import streamlit as st

def generate_social_bundle(business_name, industry, goal):
    # Récupération sécurisée de la clé
    api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    
    if not api_key:
        return "Erreur : Clé API non configurée."

    client = Groq(api_key=api_key)
    
    try:
        # UTILISATION DU MODÈLE llama-3.3-70b-versatile QUI EST ACTIF
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Tu es un expert en marketing pour artisans."},
                {"role": "user", "content": f"Fais un post Instagram pro pour l'entreprise {business_name} dans le secteur {industry}. Objectif : {goal}. Inclus des hashtags."}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur de connexion : {str(e)}"
