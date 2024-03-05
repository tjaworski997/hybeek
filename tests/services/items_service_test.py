from src.modules.services.items_service import add
from src.modules.models.item_model import ItemModel

item = ItemModel("whisli",
                 "kb",
                 "a1203",
                 ("Kraków leży nad brzegami Wisły. Jest drugim co do wielkości miastem w Polsce. "
                  "Liczba ludności w Krakowie przekracza 760 tysięcy mieszkańców. Miasto jest ważnym ośrodkiem kulturalnym i turystycznym. "
                  "W Krakowie znajduje się wiele muzeów, teatrów i galerii sztuki. W historycznej dzielnicy Kazimierz można poczuć atmosferę dawnej żydowskiej kultury. "
                  "Przez Kraków przechodzi popularny szlak turystyczny zwanym Szlakiem Orlich Gniazd. Wawel to jeden z najważniejszych zabytków Krakowa. "
                  "Kraków był niegdyś stolicą Polski. W mieście organizowane są liczne festiwale muzyczne, filmowe i teatralne. "
                  "Na terenie Krakowa znajduje się wiele parków i terenów zieleni. W Krakowie istnieje wiele legend i tradycji, związanych z historią miasta."
                  "Znajduje się tam również największy na świecie witraż wykonany przez Stanisława Wyspiańskiego. W Krakowie można zobaczyć relikwie polskiego świętego - Jana Pawła II. "
                  "W okolicach Krakowa znajduje się kopalnia soli w Wieliczce, wpisana na listę światowego dziedzictwa UNESCO. "
                  "Rocznie do Krakowa przyjeżdża miliony turystów z całego świata. W Krakowie działa wiele znanych restauracji i pubów serwujących tradycyjne dania. "
                  "W mieście znajduje się wiele pięknych kamienic z historycznymi fasadami. Kraków jest miejscem narodzin słynnego malarza Jan Matejko."
                  "Każdego roku w Krakowie odbywa się festiwal sztuki nowoczesnej - Unsound Festival."
                  ),
                 data="{}")

add(item)
