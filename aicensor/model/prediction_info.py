from . import CensorPredictionGeneralInfo
from . import CensorPredictionDetailsInfo
from . import CensorPredictionElapsedInfo


class CensorPredictionInfo:
    def __init__(self, general: CensorPredictionGeneralInfo, details: CensorPredictionDetailsInfo, elapsed: CensorPredictionElapsedInfo):
        self._general = general
        self._details = details
        self._elapsed = elapsed

    def get_general(self) -> CensorPredictionGeneralInfo:
        return self._general

    def get_details(self) -> CensorPredictionDetailsInfo:
        return self._details

    def get_elapsed(self) -> CensorPredictionElapsedInfo:
        return self._elapsed

    def __str__(self):
        return f"(general={self._general.__str__()}, details={self._details.__str__()}, elapsed={self._elapsed.__str__()})"