symptom_map = {
    "fever": "Possible Infection",
    "cough": "Respiratory Issue",
    "headache": "Neurological Symptom",
    "diabetes": "Chronic Disease",
    "chest pain": "Emergency Symptom",
    "cold": "Viral Infection",
    "fatigue": "General Weakness"
}


def detect_symptoms(text):

    text = text.lower()

    symptoms = []
    categories = []

    for symptom, category in symptom_map.items():

        if symptom in text:
            symptoms.append(symptom.title())

            if category not in categories:
                categories.append(category)

    return symptoms, categories