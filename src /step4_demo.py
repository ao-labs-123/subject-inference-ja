from typing import List, Dict

class SemanticBlock:
    def __init__(self, text: str, block_type: str):
        self.text = text
        self.block_type = block_type  # noun_phrase, verb_phrase
        self.modifiers: List[str] = []

    def add_modifier(self, modifier: str):
        self.modifiers.append(modifier)

    def __repr__(self):
        return f"{self.text} <- {self.modifiers}"


def assign_modifiers(
    modifiers: List[str],
    semantic_blocks: List[SemanticBlock],
    context_scores: Dict[str, Dict[str, float]]
):
    """
    Assign modifiers to semantic blocks based on contextual compatibility.
    """

    for modifier in modifiers:
        best_block = None
        best_score = 0.0

        for block in semantic_blocks:
            score = context_scores.get(modifier, {}).get(block.text, 0.0)

            if score > best_score:
                best_score = score
                best_block = block

        if best_block:
            best_block.add_modifier(modifier)

    return semantic_blocks


# Example usage
if __name__ == "__main__":
    blocks = [
        SemanticBlock("赤い箱", "noun_phrase"),
        SemanticBlock("ボール", "noun_phrase")
    ]

    modifiers = ["赤い", "中の"]

    context_scores = {
        "赤い": {"赤い箱": 0.9, "ボール": 0.2},
        "中の": {"赤い箱": 0.8, "ボール": 0.3}
    }

    result = assign_modifiers(modifiers, blocks, context_scores)
    for block in result:
        print(block)
