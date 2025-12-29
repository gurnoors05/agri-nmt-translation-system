import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import MarianTokenizer, MarianMTModel

print("🔄 [1/4] Starting Model Loader...")  # DEBUG PRINT

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"⚙️  Using Device: {DEVICE}")        # DEBUG PRINT

# === AGRI MODEL (exp3) ===
AGRI_MODEL_PATH = "models/final_agri_model_exp3"
print(f"📂 Loading Agri Model from: {AGRI_MODEL_PATH}") # DEBUG PRINT

try:
    agri_tokenizer = AutoTokenizer.from_pretrained(AGRI_MODEL_PATH, local_files_only=True)
    print("✅ Agri Tokenizer Loaded")         # DEBUG PRINT

    agri_model = AutoModelForSeq2SeqLM.from_pretrained(AGRI_MODEL_PATH, local_files_only=True).to(DEVICE)
    agri_model.eval()
    print("✅ Agri Model Loaded")             # DEBUG PRINT
except Exception as e:
    print(f"❌ CRASH loading Agri Model: {e}") # DEBUG PRINT
    raise e

# === FALLBACK MODEL ===
FALLBACK_NAME = "Helsinki-NLP/opus-mt-en-hi"
print(f"🌍 Loading Fallback Model: {FALLBACK_NAME}") # DEBUG PRINT

try:
    fallback_tokenizer = MarianTokenizer.from_pretrained(FALLBACK_NAME)
    print("✅ Fallback Tokenizer Loaded")     # DEBUG PRINT
    
    fallback_model = MarianMTModel.from_pretrained(FALLBACK_NAME).to(DEVICE)
    fallback_model.eval()
    print("✅ Fallback Model Loaded")         # DEBUG PRINT
except Exception as e:
    print(f"❌ CRASH loading Fallback Model: {e}") # DEBUG PRINT
    raise e

print("🎉 [2/4] All Models Ready!")           # DEBUG PRINT