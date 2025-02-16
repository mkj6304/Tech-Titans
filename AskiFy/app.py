from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import PyPDF2
import sys
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Manually add models directory to Python path
sys.path.append(os.path.abspath("models"))

# Import functions directly
from models.question_generator import generate_questions
from models.translator import translate_text
from models.answer_generator import generate_answer  # ✅ Correctly importing answer function

app = Flask(__name__)
CORS(app)  # Apply CORS to the whole app

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

extracted_text = ""
questions = []

@app.route('/upload', methods=['POST'])
def upload():
    global extracted_text

    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Save the file
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Extract text from the uploaded PDF
        extracted_text = extract_text_from_pdf(filepath)

        return jsonify({"text": extracted_text, "insights": "Key insights extracted"})
    except Exception as e:
        app.logger.error(f"Error processing file: {e}")
        return jsonify({"error": "Failed to process file"}), 500

def extract_text_from_pdf(filepath):
    """ Extract text from a PDF file """
    try:
        with open(filepath, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text if text else "No readable text found."
    except Exception as e:
        return str(e)

@app.route('/generate_questions', methods=['POST'])
def generate_questions_api():
    global questions
    if not extracted_text:
        return jsonify({"error": "No text available"}), 400

    try:
        questions = generate_questions(extracted_text)  # Call function from question_generator.py
        return jsonify({"questions": questions})
    except Exception as e:
        app.logger.error(f"Error generating questions: {e}")
        return jsonify({"error": "Failed to generate questions"}), 500

@app.route('/translate_questions', methods=['POST'])
def translate_questions():
    global questions
    data = request.json
    language = data.get("language", "en")

    translations = {
        "es": ["¿Qué es la IA?", "¿Cómo funciona el NLP?", "¿Cuáles son los desafíos del aprendizaje automático?"],
        "fr": ["Qu'est-ce que l'IA ?", "Comment fonctionne le NLP ?", "Quels sont les défis de l'apprentissage automatique?"],
        "en": questions
    }
    return jsonify({"translated_questions": translations.get(language, ["Translation not available"])})

@app.route('/generate_answers', methods=['POST'])
def generate_answers_api():
    global questions
    if not questions:
        return jsonify({"error": "No questions available to generate answers"}), 400

    answers = [generate_answer(q) for q in questions]  # Ensure function name is correct

    return jsonify({"answers": answers})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)  # ✅ Runs the app
