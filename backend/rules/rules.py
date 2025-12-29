
PESTICIDE_FERTILIZER_RULES = [
    # Wrong verb for pesticide application
    ("कीटनाशक लागू करें", "कीटनाशक का छिड़काव करें"),
    ("कीटनाशक प्रयोग करें", "कीटनाशक का छिड़काव करें"),
    ("कीटनाशक उपयोग करें", "कीटनाशक का छिड़काव करें"),

    # Wrong verb for fertilizer application
    ("उर्वरक छिड़काव करें", "उर्वरक लागू करें"),
    ("उर्वरक का छिड़काव", "उर्वरक का प्रयोग"),

    # Semantic mixing
    ("उर्वरक रोग", "कवक रोग"),
    ("कीटनाशक पोषक", "उर्वरक पोषक"),
]
SPRAY_HARD_RULES = [
        ("सिंचाई अनुप्रयोग", "छिड़काव"),
        ("स्प्रीश", "छिड़काव"),
        ("निराश करने", "छिड़काव"),
        ("छिड़काव बाधित", "छिड़काव स्थगित"),
]
PESTICIDE_NOUN_RULES = [
        ("उर्वरकों का उपयोग", "कीटनाशकों का उपयोग"),
        ("उर्वरक का प्रयोग", "कीटनाशक का प्रयोग"),
        ("उर्वरक लागू", "कीटनाशक का छिड़काव"),
]
RANDOM_CROP_HARD_RULES = [
        ("बाजरा क्षेत्रों", "हवा प्रभावित क्षेत्रों"),
        ("आलू के दौरान", "मानसून के दौरान"),
        ("चना के लिए", ""),
]
BANANA_STRUCTURE_RULES = [
        ("केला पेड़", "केले के पौधे"),
        ("केला के बीज", "केले के पौधे"),
        ("पौधों का उपयोग करें", "पौधों को सहारा दें"),
]
PORTAL_ADMIN_HARD_RULES = [
        ("कृषि अधिकारियों को", "किसानों को"),
        ("योजना कीट प्रबंधन", "योजना पंजीकरण"),
        ("रिकॉर्ड करें", "रिकॉर्ड अपलोड करें"),
]
BROKEN_HINDI_RULES = [
        ("कार्रवाई बाधित करें", "कार्रवाई स्थगित करें"),
        ("रहने का कारण", "गिरने का कारण"),
        ("उपयोग मत करें", "से बचें"),
]
STORAGE_HARD_RULES = [
        ("बाजरा का उपयोग", "एयरटाइट बैग का उपयोग"),
        ("बीजों में दालें", "डिब्बों में दालें"),
]
SPRAY_IRRIGATION_RULES = [
    # Wrong: Using irrigation verb for spraying
    ("सिंचाई करें", "छिड़काव करें"),
    ("सिंचाई का उपयोग", "छिड़काव करें"),
    ("रसायनों को सिंचाई", "रसायनों का छिड़काव"),
    ("कीटनाशक सिंचाई", "कीटनाशक का छिड़काव"),
    ("दवा सिंचाई", "दवा का छिड़काव"),

    # Context-specific: spray in evening (not irrigate)
    ("शाम के समय सिंचाई", "शाम के समय छिड़काव"),
    ("सुबह सिंचाई करें पत्ती", "सुबह छिड़काव करें"),
]
PORTAL_GOVERNMENT_RULES = [
    # Portal mistranslations
    ("कृषि बंदरगाह", "कृषि पोर्टल"),
    ("कृषि केंद्र पर अपने", "कृषि पोर्टल पर अपने"),
    ("बंदरगाह पर", "पोर्टल पर"),

    # Upload/download mistranslations
    ("लोड करें दस्तावेज़", "अपलोड करें दस्तावेज़"),
    ("डाउनलोड अपलोड", "अपलोड"),

    # Land/document terminology
    ("देश विवरण", "भूमि विवरण"),
    ("भू-अभिलेख", "भूमि अभिलेख"),
    ("ज़मीन कागजात", "भूमि दस्तावेज़"),

    # Verification terminology
    ("जाँच प्रमाण", "सत्यापन"),
    ("परीक्षण हेतु", "सत्यापन हेतु"),
]


# =============================================================================
# CATEGORY D: UPLOAD / DOCUMENT OPERATIONS
# =============================================================================
# Problem: Model generates wrong verbs for upload operations
# Context: Digital operations require specific Hindi terminology

UPLOAD_DOCUMENT_RULES = [
    # Wrong verbs for upload
    ("दस्तावेज़ प्रस्तुत", "दस्तावेज़ अपलोड"),
    ("कागजात भेजें", "कागजात अपलोड करें"),
    ("प्रमाण पत्र जमा", "प्रमाण पत्र अपलोड"),

    # Submit vs upload confusion
    ("सबमिट करें", "जमा करें"),
    ("आवेदन सबमिट", "आवेदन जमा"),
]


# =============================================================================
# CATEGORY E: BANANA / PAPAYA WIND DAMAGE
# =============================================================================
# Problem: Model hallucinates or uses wrong nouns for banana/papaya
# Context: Wind damage to banana plantations is a specific agricultural concern

BANANA_WIND_RULES = [
    # Banana hallucinations and duplications
    ("केला केला", "केले के बागान"),
    ("केला बीज", "केले के पौधे"),
    ("केला फसल", "केले की फसल"),

    # Wind-related mistranslations
    ("वायुलेटा", "तेज़ हवाएँ"),
    ("हवा केला", "केले के पौधों को हवा"),
    ("तूफान केला", "केले के बागानों को तूफान"),

    # Papaya similar issues
    ("पपीता पपीता", "पपीता के बागान"),
    ("पपीता बीज", "पपीता के पौधे"),
]


# =============================================================================
# CATEGORY F: RANDOM CROP INSERTION
# =============================================================================
# Problem: Model randomly inserts crop names where they don't belong
# Context: "मूंगफली" (groundnut) appearing in unrelated contexts

RANDOM_CROP_RULES = [
    # Groundnut (peanut) random insertion
    ("मूंगफली कीट प्रकोप", "कीट प्रकोप"),
    ("मूंगफली रोग", "रोग"),
    ("मूंगफली से बचने", "बचने"),

    # Other random crop insertions (context-dependent, apply carefully)
    # Note: Only remove if clearly wrong context
]


# =============================================================================
# CATEGORY G: IRRIGATION vs WATERLOGGING
# =============================================================================
# Problem: Model confuses irrigation terminology
# Context: "अधिक सिंचाई" = excess irrigation, "जलभराव" = waterlogging

IRRIGATION_WATERLOG_RULES = [
    # Wrong: using extension/expansion instead of excess
    ("विस्तार सिंचाई", "अधिक सिंचाई"),
    ("विस्तारित सिंचाई", "अत्यधिक सिंचाई"),

    # Waterlogging terminology
    ("पानी भराव", "जलभराव"),
    ("जल जमाव", "जलभराव"),
]


# =============================================================================
# CATEGORY H: ROOT ROT / DISEASE TERMINOLOGY
# =============================================================================
# Problem: Model uses wrong verbs for disease spread/occurrence
# Context: Diseases "होती है" (occur), not "बुवाई करता है" (sow/plant)

DISEASE_TERMINOLOGY_RULES = [
    # Wrong verbs for disease occurrence
    ("जड़ सड़न बुवाई करता है", "जड़ सड़न फैलती है"),
    ("रोग बुवाई", "रोग फैलता"),
    ("फफूंद बुवाई", "फफूंद फैलती"),

    # Root rot specific
    ("जड़ सड़न जल निकासी", "जलभराव में जड़ सड़न"),
    ("मूल रोग", "जड़ सड़न"),
]


# =============================================================================
# CATEGORY I: FERTILIZER TYPES (NPK, Urea, DAP, Potash)
# =============================================================================
# Problem: Model confuses fertilizer names and application contexts
# Context: Each fertilizer has specific uses and Hindi names

FERTILIZER_TYPES_RULES = [
    # Urea terminology
    ("यूरिया उर्वरक", "यूरिया"),

    # NPK confusion
    ("एनपीके", "NPK"),

    # Potash terminology
    ("पोटाश उर्वरक लागू", "पोटाश लागू"),

    # Zinc terminology
    ("जिंक की कमी", "जस्ता की कमी"),
    ("जिंक सल्फेट", "जस्ता सल्फेट"),
]

SPRAY_ACTION_RULES = [
    ("निराश करने से बचें", "छिड़काव से बचें"),
    ("निराश करने", "छिड़काव"),
    ("स्प्रीश", "छिड़काव"),
]
SEASON_RULES = [
    ("आलू के दौरान", "मानसून के दौरान"),
    ("फसल के दौरान", "मानसून के दौरान"),
    ("मौसम कार्यक्रम", "मौसम घटना"),
]
INSTRUCTION_COMPLETION_RULES = [
    ("फसल हानि बढ़ती है", "फसल नुकसान का विवरण अपलोड करें"),
    ("फसल नुकसान बढ़ती है", "फसल नुकसान का विवरण अपलोड करें"),
    ("नुकसान बढ़ती है", "नुकसान का विवरण अपलोड करें"),
]

# =============================================================================
# CATEGORY J: SUPERVISOR / OBSERVER HALLUCINATION
# =============================================================================
# Problem: Model inserts "सिंचाई पर्यवेक्षक" (irrigation supervisor) randomly
# Context: Instructions are for farmers, not supervisors

SUPERVISOR_HALLUCINATION_RULES = [
    ("सिंचाई पर्यवेक्षकों को", "किसानों को"),
    ("पर्यवेक्षक को", "किसानों को"),
    ("निरीक्षकों को", "किसानों को"),
]


# =============================================================================
# CATEGORY K: STORAGE / POST-HARVEST TERMINOLOGY
# =============================================================================
# Problem: Model uses wrong verbs for storage operations
# Context: "संग्रहित करें" = store, not "रखें" in formal contexts

STORAGE_RULES = [
    # Correct storage terminology
    ("भंडारण में रखें", "भंडारित करें"),
    ("स्टोर करें", "संग्रहित करें"),

    # Drying before storage
    ("सुखाने फसल", "फसल सुखाने"),
    ("कटाई के बाद सुखाने", "कटाई के बाद"),
]


# =============================================================================
# CATEGORY L: SEED TREATMENT CONFUSION
# =============================================================================
# Problem: Model confuses seed treatment with other operations
# Context: "बीज उपचार" is specific pre-sowing treatment

SEED_TREATMENT_RULES = [
    # Seed treatment terminology
    ("बीज विक्रेताओं का उपयोग", "बीज उपचार"),
    ("बीज व्यापारी", "बीज उपचार"),

    # Sowing terminology
    ("बुवाई से पहले", "बुआई से पहले"),
]


# =============================================================================
# CATEGORY M: YIELD / PRODUCTIVITY CONFUSION
# =============================================================================
# Problem: Model uses "उत्पादकता" (productivity) when meaning damage/loss
# Context: "उच्च उत्पादकता" means high productivity, opposite of damage

YIELD_PRODUCTIVITY_RULES = [
    # High productivity used wrongly for damage
    ("उच्च उत्पादकता से केला", "तेज हवाओं से केले"),
    ("उच्च उत्पादकता के दौरान", "तेज हवाओं के दौरान"),
    ("उत्पादकता नुकसान", "उपज में कमी"),
]


# =============================================================================
# CATEGORY N: WEATHER / CLIMATE TERMINOLOGY
# =============================================================================
# Problem: Model mistranslates weather-related terms
# Context: Specific Hindi terms for weather phenomena

WEATHER_RULES = [
    # Storm/wind terminology
    ("आंधी-तूफान", "तूफान"),
    ("वर्षा तूफान", "भारी वर्षा"),

    # Rainfall terminology
    ("भारी बारिश", "भारी वर्षा"),
    ("अधिक वर्षा", "अत्यधिक वर्षा"),
]
SAFETY_LANGUAGE_RULES = [
    ("सुरक्षादार वस्त्र", "सुरक्षात्मक कपड़े"),
]
HARVEST_CLEANUP_RULES = [
    ("कटाई के बाद फसल कटाई के बाद", "कटाई के बाद"),
    ("सफाई और सूखा करना चाहिए", "अच्छी तरह साफ कर सुखाना चाहिए"),
]


# =============================================================================
# CATEGORY O: SPACING / DISTANCE TERMINOLOGY
# =============================================================================
# Problem: Model uses wrong words for plant spacing
# Context: "उचित दूरी" = proper spacing/distance

SPACING_RULES = [
    # Spacing terminology
    ("फसल दूरी", "पौधों के बीच दूरी"),
    ("उचित फासला", "उचित दूरी"),
]


# =============================================================================
# CATEGORY P: SUBJECT-SPECIFIC CORRECTIONS
# =============================================================================
# Problem: Model uses wrong subjects (who does the action)
# Context: Farmers perform actions, not crops or diseases

SUBJECT_CORRECTION_RULES = [
    # Farmers as subject
    ("फसल को सुनिश्चित", "किसानों को सुनिश्चित"),
    ("पौधे को करना चाहिए", "किसानों को करना चाहिए"),
]


# =============================================================================
# CATEGORY Q: REPETITION / DUPLICATION ERRORS
# =============================================================================
# Problem: Model duplicates words
# Context: Remove unnecessary repetitions

DUPLICATION_RULES = [
    ("कटाई के बाद कटाई के बाद", "कटाई के बाद"),
    ("मृदा स्वास्थ्य सुधारने हेतु मृदा स्वास्थ्य सुधारने हेतु", "मृदा स्वास्थ्य सुधारने हेतु"),
    ("उर्वरक उर्वरक", "उर्वरक"),
]


# =============================================================================
# CATEGORY R: INCOMPLETE / BROKEN SENTENCES
# =============================================================================
# Problem: Model generates incomplete phrases
# Context: These need minimal completion, not full rewriting

INCOMPLETE_SENTENCE_RULES = [
    # Incomplete instructions
    ("बीज विक्रेताओं का उपयोग कीट प्रकोप रोकने हेतु.", "बीज उपचार करें।"),

    # Broken verb phrases
    ("को नमी से पहले रखें", "को नमी-रहित स्थान में रखें"),
]
SPRAY_SEMANTIC_RULES = [
    ("शाम को उर्वरक का प्रयोग करें", "शाम को कीटनाशक का छिड़काव करें"),
    ("रसायनों का उपयोग करें", "रसायनों का छिड़काव करें"),
]
ALL_RULES = (
    HARVEST_CLEANUP_RULES +
    SAFETY_LANGUAGE_RULES +
    SPRAY_ACTION_RULES +
    SEASON_RULES +
    INSTRUCTION_COMPLETION_RULES +
    DUPLICATION_RULES +
    INCOMPLETE_SENTENCE_RULES +
    SUBJECT_CORRECTION_RULES +
    SUPERVISOR_HALLUCINATION_RULES +
    RANDOM_CROP_RULES +
    BANANA_WIND_RULES +
    WEATHER_RULES +
    SPRAY_IRRIGATION_RULES +
    PESTICIDE_FERTILIZER_RULES +
    FERTILIZER_TYPES_RULES +
    IRRIGATION_WATERLOG_RULES +
    DISEASE_TERMINOLOGY_RULES +
    STORAGE_RULES +
    SEED_TREATMENT_RULES +
    SPACING_RULES +
    PORTAL_GOVERNMENT_RULES +
    UPLOAD_DOCUMENT_RULES +
    YIELD_PRODUCTIVITY_RULES
)
def post_correct(text: str):
    corrected = text
    applied = []
    for wrong, right in ALL_RULES:
        if wrong in corrected:
            corrected = corrected.replace(wrong, right)
            applied.append(f"{wrong} → {right}")
    corrected = " ".join(corrected.split())
    return corrected, applied
