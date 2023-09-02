# ai_module.py

questions = [
    "bonjour",
    "Comment vas-tu ?",
    "Quel est ton nom ?",
    "Quelle est la capitale de la France ?",
    # Ajoutez d'autres questions ici
]

responses = [
    "bonjour ",
    "Je vais bien, merci !",
    "Je suis un chatbot, je n'ai pas de nom.",
    "La capitale de la France est Paris.",
    # Ajoutez les réponses correspondantes aux questions ici
]
# ai_module.py

def generate_response(user_input):
    # Recherche de la question dans la liste
    if user_input in questions:
        index = questions.index(user_input)
        response = "   bot: "+ responses[index]
    else:
        response = "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler votre question ?"
    
    return response
