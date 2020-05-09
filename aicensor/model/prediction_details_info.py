class CensorPredictionDetailsInfo():
    def __init__(self, basic_contains_hit: bool, exact_match_hit: bool, ai_label: str, ai_probability: float):
        self._basic_contains_hit = basic_contains_hit
        self._exact_match_hit = exact_match_hit
        self._ai_label = ai_label
        self._ai_probability = ai_probability

    def is_basic_contains_hit(self) -> bool:
        return self._basic_contains_hit

    def is_exact_match_hit(self) -> bool:
        return self._exact_match_hit

    def get_ai_label(self) -> str:
        return self._ai_label

    def get_ai_probability(self) -> float:
        return self._ai_probability

    def __str__(self):
        return f"(basic_contains_hit={self._basic_contains_hit}, exact_match_hit={self._exact_match_hit}, ai_label={self._ai_label}, ai_probability={self._ai_probability})"
