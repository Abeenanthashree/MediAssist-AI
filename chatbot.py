def get_bot_response(message):

    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! I am MediAssist AI. How can I help you?"

    elif "fever" in msg:
        return "Fever may indicate an infection. Please consult a healthcare professional if symptoms persist."

    elif "headache" in msg:
        return "Headaches can be caused by stress, dehydration, or illness. Stay hydrated and rest."

    elif "cough" in msg:
        return "A cough may be associated with a cold, allergy, or infection."

    elif "cold" in msg:
        return "Common cold symptoms often improve with rest and hydration."

    elif "medicine" in msg:
        return "Please take medicines only as prescribed by your doctor."

    elif "appointment" in msg:
        return "You can contact your nearest healthcare provider to schedule an appointment."

    elif "emergency" in msg:
        return "For emergencies, contact emergency medical services immediately."

    elif "bye" in msg:
        return "Take care and stay healthy."

    else:
        return "I can help with symptoms, medicines, appointments, and healthcare information."
