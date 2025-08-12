
from transformers import pipeline
import torch

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
ner = pipeline("ner", model="dslim/bert-base-NER")

def summarize_text(text: str) -> str:
    try:
        summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Error in summarization: {e}"

def extract_medical_keywords(text: str):
    try:
        entities = ner(text)
        keywords = list(set([ent['word'] for ent in entities if ent['score'] > 0.5]))
        return keywords
    except Exception as e:
        return [f"Error in keyword extraction: {e}"]

# AI-based summarization service stub
def generate_doctor_questions(lab_results, medicines):
    questions = []
    # Suggest HbA1c if glucose is high
    high_glucose = any(r.get("param") == "Glucose" and r.get("status") == "high" for r in lab_results)
    if high_glucose:
        questions.append("Should I get an HbA1c test?")
    # Ask about antibiotics if prescribed without infection marker
    antibiotics = [m for m in medicines if m.get("name").lower() in ["amoxicillin", "azithromycin"]]
    infection_marker = any(r.get("param") == "WBC" and r.get("status") == "high" for r in lab_results)
    if antibiotics and not infection_marker:
        questions.append("Is this antibiotic necessary without infection markers?")
    # Add more rules as needed
    return questions
