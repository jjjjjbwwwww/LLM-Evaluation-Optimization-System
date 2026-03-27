


import re

def parse_score(text):
    scores = {}

    for key in ["correctness", "relevance", "completeness"]:
        match = re.search(f"{key}: (0\\.\\d+|1\\.0)", text)
        if match:
            scores[key] = float(match.group(1))
        else:
            scores[key] = 0.0

    scores["total"] = sum(scores.values()) / len(scores)
    return scores