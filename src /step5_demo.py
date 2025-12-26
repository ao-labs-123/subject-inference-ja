class CaseRelationEstimator:
    def __init__(self, verb_case_frames):
        """
        verb_case_frames:
        {
            "送る": ["agent", "object", "recipient"],
            "行く": ["agent", "location"],
            ...
        }
        """
        self.verb_case_frames = verb_case_frames

    def estimate(self, parsed_sentence):
        """
        parsed_sentence: list of tokens
        token = {
            "surface": str,
            "pos": str,
            "particle": str | None,
            "head_verb": str | None
        }
        """
        relations = []

        for token in parsed_sentence:
            if token["pos"] == "NOUN" and token["particle"]:
                case = self._infer_case(token["particle"])
                verb = token["head_verb"]

                confidence = self._validate_case(verb, case)

                relations.append({
                    "noun": token["surface"],
                    "verb": verb,
                    "case": case,
                    "confidence": confidence
                })

        return relations

    def _infer_case(self, particle):
        case_map = {
            "が": "agent",
            "を": "object",
            "に": "recipient",
            "で": "location_or_means",
            "へ": "direction",
            "から": "source",
            "まで": "goal"
        }
        return case_map.get(particle, "unknown")

    def _validate_case(self, verb, case):
        if verb not in self.verb_case_frames:
            return 0.5  # unknown verb

        if case in self.verb_case_frames[verb]:
            return 0.9  # valid relation
        else:
            return 0.3  # suspicious or weak relation
