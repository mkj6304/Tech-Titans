AskiFY - AI-Powered Multilingual Q&A Generator 🌍🤖

 Transform PDFs into AI-Generated Insights, Questions & Answers!
AskiFY is an AI-powered multilingual question-answering system that allows users to:
 Upload a PDF and extract text.
 Translate the extracted text into multiple languages.
 Generate AI-based questions from the extracted content.
 Answer user questions using an AI model.
 Seamlessly interact with an intuitive UI.

 Features
 PDF Text Extraction - Extracts text from PDFs with high accuracy.
 Multilingual Support - Translates text into multiple languages (English, Spanish, Hindi, French, etc.).
 AI-Based Question Generation - Generates meaningful questions from the extracted text using OpenAI's API.
 AI-Powered Answer Generation - Provides AI-generated answers for user questions.
 Fast & Efficient - Backend built with Flask and powered by AI.
 User-Friendly Interface - Simple and easy-to-use UI with Bootstrap for responsiveness.
 Project Structure:-

Copy
Edit
AskiFY/
│── static/               # Static files (CSS, JS, images)
│   ├── script.js         # Frontend JavaScript functions
│   ├── styles.css        # Stylesheet for UI
│   ├── logo.jpg          # Project logo
│── templates/            # HTML templates
│   ├── index.html        # Main UI
│── uploads/              # Stores uploaded PDFs
│── app.py                # Flask backend
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
🛠️ Tech Stack & Libraries Used
Frontend (User Interface)
HTML, CSS, JavaScript - Webpage structure and styling.
Bootstrap - Responsive UI components.
Fetch API - Handles async communication with backend.
Backend (Flask API)
Flask - Python web framework for API endpoints.
Flask-CORS - Enables Cross-Origin Resource Sharing.
PDF Processing
PyMuPDF (fitz) - Extracts text from PDFs.
pdfplumber (Alternative) - Better text extraction for scanned PDFs.
Translation
googletrans (Google Translate API) - Provides text translation in multiple languages.
AI-Based Processing
OpenAI API (GPT-4, GPT-3.5) - Generates questions and answers based on extracted text.
Deployment
Gunicorn - Production-ready Flask server.
Render/Heroku - Cloud deployment options.
💻 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/AskiFY.git
cd AskiFY
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy
Edit
python app.py
🚀 The app will be live at http://127.0.0.1:5000/

📝 How It Works?
1️⃣ Upload PDF
Click "Choose File" and select a PDF.
Click "Upload & Extract" to extract text.
2️⃣ Translate Text
Select a language from the dropdown.
Click "Translate" to convert extracted text.
3️⃣ Generate Questions
Click "Generate Questions" to create AI-based questions.
4️⃣ Ask a Question
Type your question and click "Ask" to receive an AI-generated answer.
📸 Screenshots

🚀 Deployment
Using Gunicorn for Production
bash
Copy
Edit
gunicorn -w 4 app:app
Deploy to Heroku
bash
Copy
Edit
heroku create askify-app
git push heroku main
📌 Future Improvements
🔹 Add OCR support for scanned PDFs.
🔹 Implement speech-to-text for voice-based Q&A.
🔹 Enhance UI/UX for better user experience.

👨‍💻 Contributors
Your Name (Developer & AI Engineer)
Team Members (If any)
📜 License
MIT License. Feel free to use, modify, and contribute!

🚀 Enjoy using AskiFY! 😊