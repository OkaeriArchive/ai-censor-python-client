class CensorPredictionGeneralInfo():
    def __init__(self, swear: bool, breakdown: str):
        self._swear = swear
        self._breakdown = breakdown

    def is_swear(self) -> bool:
        return self._swear

    def get_breakdown(self) -> str:
        return self._breakdown

    def __str__(self):
        return f"(swear={self._swear}, breakdown={self._breakdown})"
