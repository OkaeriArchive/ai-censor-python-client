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