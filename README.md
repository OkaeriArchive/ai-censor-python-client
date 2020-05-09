# OK! AI.Censor Python Client
Implementacja publicznego API OK! AI.Censor w Pythonie (3.5+).
```
pip install git+https://github.com/OkaeriPoland/ai-censor-python-client#egg=aicensor
```

## Przykładowe użycie
```python
from aicensor import AiCensorClient
from aicensor.errors import AiCensorError

token = "xxx" # dane uwierzytelniające
censor = AiCensorClient(token) # tworzymy klienta (w większości przypadków należy go gdzieś zapisać)

# proste zapytanie
try:
    swear = censor.is_swear("o cie k u r//w@!")
    print("Tak, to jest wulgarne." if swear else "Nie, to nie jest wulgarne.")
except AiCensorError as err:
    print(f"Cos poszlo nie tak: {str(err)}")

# pelne zapytanie
try:
    prediction = censor.get_prediction("o cie k u r//w@!")
    print(prediction)
except AiCensorError as err:
    print(f"Cos poszlo nie tak: {str(err)}")
```

## Opis zwracanych własności

#### aicensor.model.CensorPredictionInfo

| Własność  | Opis |
| ------------- | ------------- |
| #get_general() -> CensorPredictionGeneralInfo | Sekcja ogólna odpowiedzi |
| #get_details() -> CensorPredictionDetailsInfo | Sekcja szczegółów odpowiedzi |
| #get_elapsed() -> CensorPredictionElapsedInfo | Sekcja informacji dotyczących czasu przetwarzania |


#### aicensor.model.CensorPredictionGeneralInfo

| Własność  | Opis |
| ------------- | ------------- |
| #is_swear() -> bool           | Informacja o tym, czy wiadomość została uznana za wulgarną |
| #get_breakdown() -> str       | Przetworzona wiadomość ułatwiająca ewentualne debugowanie błędnych wykryć, przydatna do wyświetlania dla administracji w logach |


#### aicensor.model.CensorPredictionDetailsInfo

| Własność  | Opis |
| ------------- | ------------- |
| #is_basic_contains_hit() -> bool | Informacja o tym, czy wiadomość zawierała zakazane frazy |
| #is_exact_match_hit() -> bool    | Informacja o tym, czy wiadomość była zablokowaną frazą (np. wyrażenie jd) |
| #get_ai_label() -> str           | Ocena ai (`ok` lub `swear`) |
| #get_ai_probability() -> float   | Wartość od `0` do `1` określająca prawdopodobieństwo dotyczące prawdziwości `aiLabel` |


#### aicensor.model.CensorPredictionElapsedInfo

| Własność  | Opis |
| ------------- | ------------- |
| #get_all() -> float           | Całkowity czas w milisekundach przez który zapytanie było obsługiwane wewnętrznie |
| #get_processing() -> float    | Czas przez jaki zostały wykonane oceny wulgarności |