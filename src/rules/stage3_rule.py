
import json
from pathlib import Path

def get_lexicon():
    lexicon_path = Path(__file__).resolve().parent.parent / "lexicon" / "causality_markers.json"
    with lexicon_path.open("r", encoding="utf-8") as f:
        causality_list = json.load(f)
    return causality_list

def analyze_causality(text):
    lexicon = get_lexicon()

    is_causal = any(marker.lower() in text.lower() for marker in lexicon)
    return is_causal
