INTENT_OVERRIDES = [
    {
        "en_keywords": ["postpone", "spray", "rain"],
        "hi": "लगातार वर्षा के कारण कीटनाशक छिड़काव को स्थगित करने की सलाह दी जाती है।"
    },
    {
        "en_keywords": ["waterlogging", "fungal"],
        "hi": "जलभराव की स्थिति में फसलों में कवक रोगों का खतरा बढ़ सकता है।"
    },
    {
        "en_keywords": ["low-lying", "drainage"],
        "hi": "निचले क्षेत्रों में खड़ी फसल की सुरक्षा के लिए उचित जल निकासी सुनिश्चित करें।"
    },
    {
        "en_keywords": ["children", "animals", "sprayed"],
        "hi": "छिड़काव किए गए खेतों में बच्चों और पशुओं को तुरंत प्रवेश न करने दें।"
    },
    {
        "en_keywords": ["seeds", "grains", "separately"],
        "hi": "बीज और अनाज को अलग-अलग, साफ और हवादार कमरों में संग्रहित करें।"
    },
    {
        "en_keywords": ["portal", "advisories"],
        "hi": "किसानों को कृषि पोर्टल पर अपलोड की गई आधिकारिक सलाहों की नियमित जांच करनी चाहिए।"
    }
]

POLICY_KEYWORDS = [
    "crore","₹","rs","dbt","installment","scheme","pm-kisan",
    "beneficiary","aadhaar","ekyc","portal","budget","subsidy"
]

AGRI_KEYWORDS = [
    "fertilizer","urea","potash","npk","soil","crop","spray",
    "pesticide","fungal","irrigation","drainage","disease",
    "harvest","seed","banana","papaya","wheat","rice"
]

def intent_override(sentence: str):
    s = sentence.lower()
    for rule in INTENT_OVERRIDES:
        if all(k in s for k in rule["en_keywords"]):
            return rule["hi"]
    return None

def should_use_agri_model(sentence: str) -> bool:
    s = sentence.lower()
    if any(k in s for k in AGRI_KEYWORDS):
        return True
    if any(k in s for k in POLICY_KEYWORDS):
        return False
    return True
