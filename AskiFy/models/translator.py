from googletrans import Translator

def translate_text(text, target_language="fr"):
    """Translate text into a target language."""
    translator = Translator()
    return translator.translate(text, dest=target_language).text

if __name__ == "__main__":
    question = "When was the Eiffel Tower built?"
    translated_question = translate_text(question, "es")  # Translate to Spanish
    
    print("Original:", question)
    print("Translated:", translated_question)
