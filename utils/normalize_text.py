def normalize_text(text):
    slang_dict = {
        "u": "you", "ur": "your", "gr8": "great", "b4": "before",
        "luv": "love", "4ever": "forever", "omg": "oh my god", "plz": "please"
    }
    words = text.lower().split()
    normalized = [slang_dict.get(word, word) for word in words]
    return " ".join(normalized)