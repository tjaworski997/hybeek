from src.api.modules.content.content_cleaner_service import clean_content
from src.api.modules.content.sentences_service import get_sentences_from_content

text = ("Kraków leży nad brzegami Wisły. Jest drugim co do wielkości miastem w Polsce. "
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
        )

sentences = get_sentences_from_content(text)

for s in sentences:
    print(s)

sentences_cleaned = []

for s in sentences:
    sentences_cleaned.append(clean_content(s, "Spacy", False))

for s in sentences_cleaned:
    print(s)
