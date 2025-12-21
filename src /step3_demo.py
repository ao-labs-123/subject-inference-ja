from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Event:
    """
    Represents an extracted event or state.
    """
    id: int
    description: str
    time_index: int  # relative order in the utterance


@dataclass
class CausalRelation:
    """
    Represents a causal hypothesis between two events.
    """
    cause: Event
    effect: Event
    confidence: float
    is_confirmed: bool


class CausalInferenceEngine:
    """
    Stage 3: Causal Relationship Inference Engine
    """

    def __init__(self):
        pass

    def extract_events(self, text: str) -> List[Event]:
        """
        Naive event extraction.
        In practice, this will be replaced by NLP-based extraction.
        """
        sentences = [s.strip() for s in text.split("、") if s.strip()]
        events = []

        for idx, sentence in enumerate(sentences):
            events.append(Event(
                id=idx,
                description=sentence,
                time_index=idx
            ))

        return events

    def generate_causal_candidates(
        self, events: List[Event]
    ) -> List[Tuple[Event, Event]]:
        """
        Generate causal candidates based on temporal order.
        """
        candidates = []

        for i in range(len(events)):
            for j in range(i + 1, len(events)):
                candidates.append((events[i], events[j]))

        return candidates

    def evaluate_causality(
        self, cause: Event, effect: Event
    ) -> CausalRelation:
        """
        Evaluate plausibility of a causal relationship.
        This version uses heuristic scoring.
        """

        # Simple heuristic: earlier events are more likely causes
        time_score = 1.0 if cause.time_index < effect.time_index else 0.3

        # Keyword-based adjustment (placeholder logic)
        keywords = ["because", "so", "therefore", "result"]
        keyword_score = 1.0 if any(k in effect.description.lower() for k in keywords) else 0.6

        confidence = round((time_score + keyword_score) / 2, 2)

        return CausalRelation(
            cause=cause,
            effect=effect,
            confidence=confidence,
            is_confirmed=confidence >= 0.75
        )

    def infer(self, text: str) -> List[CausalRelation]:
        """
        Main inference pipeline.
        """
        events = self.extract_events(text)
        candidates = self.generate_causal_candidates(events)

        relations = []
        for cause, effect in candidates:
            relation = self.evaluate_causality(cause, effect)
            relations.append(relation)

        return relations

Example Usage
if __name__ == "__main__":
    engine = CausalInferenceEngine()

    text = "雨が降っていた、道が滑りやすかった、転んだ"
    results = engine.infer(text)

    for r in results:
        print(
            f"CAUSE: {r.cause.description} -> EFFECT: {r.effect.description} "
            f"(confidence={r.confidence}, confirmed={r.is_confirmed})"
        )
