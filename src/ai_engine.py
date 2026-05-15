from groq import Groq
import os

def generate_social_bundle(business_name, industry, goal):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    prompt = f"""
    Expert marketing pour artisans. Entreprise: {business_name}. Secteur: {industry}. Objectif: {goal}.
    Rédige un post Instagram/Facebook haut de gamme :
    - Accroche puissante
    - Corps du texte valorisant le savoir-faire
    - Appel à l'action pour devis
    - 5 hashtags stratégiques
    """
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur : {str(e)}"
