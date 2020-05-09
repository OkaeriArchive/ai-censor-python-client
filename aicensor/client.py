import json
import requests

from .errors import AiCensorError
from .model import *


class AiCensorClient():
    def __init__(self, token: str, base_url: str = "https://ai-censor.okaeri.eu"):
        self._baseUrl = base_url
        self._token = token

    def is_swear(self, phrase) -> bool:
        return self.get_prediction(phrase).get_general().is_swear()

    def get_prediction(self, phrase) -> CensorPredictionInfo:

        try:
            request = requests.post(url=f"{self._baseUrl}/predict",
                                    json={'phrase': phrase},
                                    headers={'Token': self._token})
        except requests.exceptions.RequestException as exception:
            raise AiCensorError("REQUEST_ERROR", str(exception))

        try:
            _json = request.json()
        except json.decoder.JSONDecodeError as error:
            raise AiCensorError('REQUEST_ERROR', f"Server returned invalid json: {str(error)}")

        if request.status_code != 200:
            if ('type' in _json) and ('message' in _json):
                raise AiCensorError(_json['type'], _json['message'])
            else:
                raise AiCensorError("UNKNOWN_ERROR", request.text)

        general = CensorPredictionGeneralInfo(_json['general']['swear'],
                                              _json['general']['breakdown'])

        details = CensorPredictionDetailsInfo(_json['details']['basic_contains_hit'],
                                              _json['details']['exact_match_hit'],
                                              _json['details']['ai_label'],
                                              _json['details']['ai_probability'])

        elapsed = CensorPredictionElapsedInfo(_json['elapsed']['all'],
                                              _json['elapsed']['processing'])

        return CensorPredictionInfo(general, details, elapsed)
