from src.modules.services.items_service import add_or_update, delete, add_or_update
from src.modules.models.item_model import ItemModel

item = ItemModel("whisli",
                 "kb",
                 "a1203",
                 ("Kraków leży nad brzegami Wisły. Jest drugim co do wielkości miastem w Polsce. "
                  "Liczba ludności w Krakowie przekracza 760 tysięcy mieszkańców. Miasto jest ważnym ośrodkiem kulturalnym i turystycznym. "
                 
                  ),
                 data="{}")

add_or_update(item)

# delete("whisli", "kb", "a1203")
