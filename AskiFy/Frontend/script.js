document.addEventListener("DOMContentLoaded", function () {
    const uploadInput = document.getElementById("uploadInput");
    const uploadButton = document.getElementById("uploadButton");
    const generateButton = document.getElementById("generateButton");
    const translateButton = document.getElementById("translateButton");
    const languageSelect = document.getElementById("languageSelect");
    //const backendURL = "http://127.0.0.1:5000";  // Make sure this is defined at the top
    const extractedTextArea = document.getElementById("extractedText");
    const insightsArea = document.getElementById("insights");
    const questionsArea = document.getElementById("questions");
    const translatedQuestionsArea = document.getElementById("translatedQuestions");

    const backendURL = "http://127.0.0.1:5000";  // Ensure this matches your Flask URL

    // Upload PDF & Extract Text
    uploadButton.addEventListener("click", function () {
        let formData = new FormData();
        let file = uploadInput.files[0];

        if (!file) {
            alert("Please select a PDF file to upload.");
            return;
        }

        formData.append("file", file);

        fetch(`${backendURL}/upload`, {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                extractedTextArea.textContent = data.text;
                insightsArea.textContent = data.insights;
            }
        })
        .catch(error => console.error("Upload Error:", error));
    });

    // Generate Questions
    generateButton.addEventListener("click", function () {
        fetch(`${backendURL}/generate_questions`, {
            method: "POST"
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                questionsArea.innerHTML = "";
                data.questions.forEach(q => {
                    let p = document.createElement("p");
                    p.textContent = q;
                    questionsArea.appendChild(p);
                });
            }
        })
        .catch(error => console.error("Fetch error:", error));
    });

    // Translate Questions
    translateButton.addEventListener("click", function () {
        let selectedLanguage = languageSelect.value;

        fetch(`${backendURL}/translate_questions`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ language: selectedLanguage })
        })
        .then(response => response.json())
        .then(data => {
            translatedQuestionsArea.innerHTML = "";
            data.translated_questions.forEach(q => {
                let p = document.createElement("p");
                p.textContent = q;
                translatedQuestionsArea.appendChild(p);
            });
        })
        .catch(error => console.error("Fetch error:", error));
    });
});

const backendURL = "http://127.0.0.1:5000";  // Make sure this is defined at the top

document.getElementById("answerButton").addEventListener("click", function () {
    fetch(`${backendURL}/generate_answers`, {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const answersArea = document.getElementById("answers");
            answersArea.innerHTML = ""; // Clear previous answers
            data.answers.forEach(ans => {
                let p = document.createElement("p");
                p.textContent = ans;
                answersArea.appendChild(p);
            });
        }
    })
    .catch(error => console.error("Error:", error));
});
