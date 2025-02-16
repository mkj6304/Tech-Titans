from transformers import pipeline

def generate_questions(text, num_questions=3):
    """Generate questions from text using the T5 model."""
    try:
        # Load the T5 question generation model
        qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-small-qg-hl")

        # Format text for the model
        formatted_text = "highlight: " + text + " </s>"

        # Generate questions using beam search
        questions = qg_pipeline(
            formatted_text,
            max_length=128,
            num_return_sequences=num_questions,
            num_beams=5  # Enable beam search with 5 beams
        )

        return [q["generated_text"] for q in questions]
    except Exception as e:
        return [f"Error generating questions: {str(e)}"]

if __name__ == "__main__":
    sample_text = "The Eiffel Tower was built in 1889 and is located in Paris, France."
    questions = generate_questions(sample_text)

    print("Generated Questions:")
    for i, q in enumerate(questions, 1):
        print(f"{i}. {q}")
