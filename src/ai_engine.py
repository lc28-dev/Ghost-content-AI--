from groq import Groq
import os

def generate_social_bundle(business_name, industry, goal):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    # Prompt ultra-détaillé pour les artisans
    prompt = f"""
    Tu es le meilleur expert en marketing digital pour artisans. 
    Crée un post incroyable pour l'entreprise {business_name} dans le secteur {industry}.
    L'objectif est : {goal}.
    
    Structure du post :
    1. Une accroche choc (Hook)
    2. Le corps du post qui valorise le savoir-faire et la qualité du travail
    3. Une liste à puces des bénéfices clients
    4. Un appel à l'action (CTA) clair pour demander un devis
    5. 5 hashtags pertinents.
    """
    
    try:
        # MISE À JOUR DU MODÈLE ICI
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur technique : {str(e)}"

