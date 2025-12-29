# 🌾 Agri NMT Translation System (English → Hindi)

This project presents a domain-specific Neural Machine Translation (NMT) system
for translating agricultural advisories from English to Hindi.

## 🔹 Key Features
- Transformer-based NMT model
- Progressive fine-tuning (Exp1 → Exp3)
- Domain-specific post-correction rules
- Intent override for critical advisories
- Domain gating with fallback translation
- FastAPI backend
- React + Tailwind frontend

## 🔹 Architecture
Input Text → Sentence Splitter → Neural Translation →
Rule-Based Correction → Final Hindi Output

## 🔹 Models Used
- Base Model: Helsinki-NLP/opus-mt-en-hi
- Fine-tuned on agricultural datasets
- Hybrid neural + rule-based pipeline

## 🔹 Tech Stack
- Python, PyTorch, HuggingFace Transformers
- FastAPI (Backend API)
- React + Tailwind CSS (Frontend)
- Google Colab (Training)

## 🔹 Disclaimer
Trained model files and datasets are not included due to size constraints.
Instructions to reproduce training are provided in the report.

