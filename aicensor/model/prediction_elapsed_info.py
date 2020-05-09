class CensorPredictionElapsedInfo():
    def __init__(self, all: float, processing: float):
        self._all = all
        self._processing = processing

    def get_all(self) -> float:
        return self._all

    def get_processing(self) -> float:
        return self._processing

    def __str__(self):
        return f"(all={self._all}, processing={self._processing})"
