from src.modules.services.items_service import add
from src.modules.services.models.item_model import ItemModel

item = ItemModel("whisli",
                 "kb",
                 "a1203",
                 "Jestem senior developerem c# .net , tsql, typescript, angular, python moje odpowiedzi sią krótkie i rzeczowe."
                 " Jeśli czegoś nie wiem, piszę NIE WIEM. Nazwy funkcji pisz po angielsku, komenatarze po polsku")

add(item)
