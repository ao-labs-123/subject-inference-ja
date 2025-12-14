Code Example

◇state.py
from typing import List, Optional

class InterpretationState:
    def __init__(self):
        self.subject_candidates: List[str] = []
        self.confirmed_subject: Optional[str] = None
        self.is_ambiguous: bool = False

◇detector.py
def detect_subject_ambiguity(text: str) -> list[str]:
    """
    Detects potential subject candidates.
    This implementation is intentionally conservative.
    """

    # Placeholder logic (to be replaced with NLP pipeline)
    if "was" in text or "だった" in text:
        return ["user", "other"]

    return []

◇clarifier.py
def generate_clarification(candidates: list[str]) -> str:
    """
    Generates a minimal clarification question.
    """

    if "user" in candidates:
        return "Are you referring to something that happened to you personally?"

    return "Could you clarify who or what you are referring to?"

◇stage2.py
from stage2.detector import detect_subject_ambiguity
from stage2.clarifier import generate_clarification
from stage2.state import InterpretationState


def process_stage2(text: str) -> dict:
    state = InterpretationState()
    candidates = detect_subject_ambiguity(text)

    if len(candidates) > 1:
        state.is_ambiguous = True
        state.subject_candidates = candidates

        return {
            "status": "clarification_required",
            "question": generate_clarification(candidates),
            "state": state,
        }

    return {
        "status": "pass_through",
        "text": text,
    }

◇Example Execution

input_text = "Yesterday was really tough."

result = process_stage2(input_text)

print(result["status"])
print(result["question"])

◇Output
clarification_required
Are you referring to something that happened to you personally?



