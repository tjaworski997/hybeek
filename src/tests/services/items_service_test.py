from src.api.modules.models.item_model import ItemModel
from src.api.modules.services.items_service import add_or_update

item1 = ItemModel("whisli",
                  "kb",
                  "a1203",
                  ("Kraków leży nad brzegami Wisły. Jest drugim co do wielkości miastem w Polsce. "
                   "Liczba ludności w Krakowie przekracza 760 tysięcy mieszkańców. Miasto jest ważnym ośrodkiem kulturalnym i turystycznym. Programowanie w dotnecie"

                   ),
                  data="{}")

item2 = ItemModel("whisli",
                  "kb",
                  "a1204",
                  ("Czasem lepiej jest nie wiedzieć, co się dzieje wokół nas. Programowanie w c# "

                   ),
                  data="{}")

item3 = ItemModel("whisli",
                  "kb",
                  "a1205",
                  ("Stół z powyłamywanymi nogami. Programowanie w pythonie. "
                   ),
                  data="{}")

add_or_update(item1)
add_or_update(item2)
add_or_update(item3)

# delete("whisli", "kb", "a1203")
