from groq import Groq
import os

def generate_social_bundle(business_name, industry, goal):
    # Utilise la clé API Groq (gratuite)
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    prompt = f"Tu es un expert en marketing. Crée un post pro pour {business_name} ({industry}). Style: {goal}."
    
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erreur de connexion : {str(e)}"
