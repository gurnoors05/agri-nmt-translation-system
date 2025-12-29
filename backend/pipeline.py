import re, torch
from model_loader import (
    agri_model, agri_tokenizer,
    fallback_model, fallback_tokenizer, DEVICE
)
from rules.intent import intent_override, should_use_agri_model
from rules.rules import post_correct

# In pipeline.py
def split_sentences(text: str):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]  # <--- Added this filter to match Colab

def agri_translate(sentence: str):
    inputs = agri_tokenizer(sentence, return_tensors="pt", truncation=True).to(DEVICE)
    with torch.no_grad():
        output = agri_model.generate(**inputs, max_length=64, num_beams=4)
    return agri_tokenizer.decode(output[0], skip_special_tokens=True)

def fallback_translate(sentence: str):
    inputs = fallback_tokenizer(sentence, return_tensors="pt", truncation=True).to(DEVICE)
    with torch.no_grad():
        output = fallback_model.generate(**inputs, max_length=128, num_beams=4)
    return fallback_tokenizer.decode(output[0], skip_special_tokens=True)

def agri_translate_pipeline(text: str):
    sentences = split_sentences(text)
    final = []

    for s in sentences:
        # 1️⃣ Intent override
        intent = intent_override(s)
        if intent:
            final.append(intent)
            continue

        # 2️⃣ Domain gate
        if not should_use_agri_model(s):
            final.append(fallback_translate(s))
            continue

        # 3️⃣ Agri + rules
        raw = agri_translate(s)
        hi, _ = post_correct(raw)
        final.append(hi)

    return " ".join(final)
