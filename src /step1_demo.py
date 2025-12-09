# Step 1 Prototype Implementation
# Basic sentence decomposition demo

def decompose(sentence: str) -> dict:
    """
    Very simple prototype for Step 1.
    Separates: subject / target / object based on patterns.
    """
    result = {
        "subject": None,
        "target": None,
        "object": None,
        "notes": []
    }

    # 例として「〜に」「〜を」を簡易抽出
    if "に" in sentence:
        parts = sentence.split("に", 1)
        result["target"] = parts[0].strip()
        sentence = parts[1]

    if "を" in sentence:
        parts = sentence.split("を", 1)
        result["object"] = parts[0].strip()
        sentence = parts[1]

    # 主語は省略 → 仮に「私」
    result["subject"] = "私"

    return result


if __name__ == "__main__":
    test = "昨日会った友達に本を渡したい"
    print(decompose(test))
